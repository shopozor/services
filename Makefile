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

dev-test.unit:
	# Unit tests
	@make --directory backend test.unit
	@npx lerna run test:unit --stream

dev-test.setup:
	@make --directory backend build
	@make bootstrap
	@make --directory backend fixtures.generate
	@make --directory backend up

dev-test.run-backend:
	# Integration tests
	@make --directory backend assets.up
	@make --directory backend seed-database
	@make --directory backend test.integration
	@make --directory backend unseed-database
	@make --directory backend assets.down

dev-test.run-frontend:
	# Integration tests
	@make --directory frontend dev-test.integration
	# E2e tests
	@make --directory backend assets.up
	@make --directory backend seed-database
	@make --directory frontend dev-test.e2e
	@make --directory backend unseed-database
	@make --directory backend assets.down

dev-test.all: down dev-test.setup dev-test.unit dev-test.run-backend dev-test.run-frontend down
dev-test.backend: down dev-test.setup dev-test.run-backend down
dev-test.frontend: down dev-test.setup dev-test.run-frontend down

test.unit:
	@docker-compose -f ./docker-compose-tests.yaml up --abort-on-container-exit jest-unit-tests