bootstrap:
	@yarn
	@yarn bootstrap

build:
	@echo "Building images..."
	@docker-compose build

down:
	@docker-compose down --remove-orphans

lint:
	@./scripts/check_linting.sh

dev-test.unit:
	# Unit tests
	# TODO: this will not work anymore!
	@make --directory backend test
	@npx lerna run test:unit --stream

dev-test.setup:
	@make build
	@make bootstrap
	@make --directory backend fixtures.generate
	devspace run cleanup-fixtures
	devspace run cleanup-assets

dev-test.run-backend:
	# Integration tests
	devspace run push-assets
	devspace run push-fixtures
	# TODO: this will not work anymore!
	@make --directory backend test
	devspace run cleanup-fixtures
	devspace run cleanup-assets

dev-test.run-frontend:
	# Integration tests
	# TODO: this will not work anymore!
	@make --directory frontend dev-test.integration
	# E2e tests
	devspace run push-assets
	devspace run push-fixtures
	# TODO: this will not work anymore!
	@make --directory frontend dev-test.e2e
	devspace run cleanup-fixtures
	devspace run cleanup-assets

dev-test.all: down dev-test.setup dev-test.unit dev-test.run-backend dev-test.run-frontend down
dev-test.backend: down dev-test.setup dev-test.run-backend down
dev-test.frontend: down dev-test.setup dev-test.run-frontend down

test.unit:
	@docker-compose -f ./docker-compose.yaml up --abort-on-container-exit jest-unit-tests