bootstrap:
	@yarn
	@yarn bootstrap

build:
	make --directory backend build
	make --directory frontend build

down:
	make --directory backend down
	make --directory frontend down

lint:
	@./scripts/check_linting.sh

dev.backend.start:
	@make --directory backend dev.start

dev.backend.end:
	@make --directory backend dev.end

dev-test.setup:
	@make --directory backend build
	@make bootstrap
	@make --directory backend fixtures.generate
	@make --directory backend up

dev-test.run-backend:
	# Unit tests
	@make --directory backend test.unit
	# Integration tests
	@make --directory backend seed-database
	@make --directory backend test.integration
	@make --directory backend unseed-database

dev-test.run-frontend:
	# Unit tests
	@make --directory frontend dev-test.unit
	# Integration tests
	@make --directory frontend dev-test.integration
	# E2e tests
	@make --directory backend seed-database
	@make --directory frontend dev-test.e2e
	@make --directory backend unseed-database

dev-test.all: down dev-test.setup dev-test.run-backend dev-test.run-frontend down
dev-test.backend: down dev-test.setup dev-test.run-backend down
dev-test.frontend: down dev-test.setup dev-test.run-frontend down