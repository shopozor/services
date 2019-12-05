dev.start.admin: init
	@make --directory .. dev.backend.start
	@lerna run start:dev --scope admin-ui

dev.start.consumer: init
	@make --directory .. dev.backend.start
	@lerna run start:dev --scope consumer-ui

dev.start.all: init
	@make --directory .. dev.backend.start
	@lerna run start:dev

init:
	@make --directory .. bootstrap

dev.end:
	@make --directory .. dev.backend.end

test.admin-unit:
	@lerna run test:unit --scope admin-ui

test.consumer-unit:
	@lerna run test:unit --scope consumer-ui

test.admin-integration:
	@lerna run cypress:integration --scope admin-ui

test.consumer-integration:
	@lerna run cypress:integration --scope consumer-ui

test.admin-e2e:
	@lerna run cypress:e2e --scope admin-ui

test.consumer-e2e:
	@lerna run cypress:e2e --scope consumer-ui

up:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml up -d consumer-ui admin-ui

build:
	@echo "Building images..."
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml build

down:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml down --remove-orphans

rm:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml rm -f

test.unit:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml up --abort-on-container-exit ui-unit-tests

test.integration:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml up --abort-on-container-exit ui-integration-tests

test.e2e:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml up --abort-on-container-exit e2e-tests

test: build test.unit test.integration test.e2e
test.cleanup: down rm

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

%.logs:
	docker-compose logs -f $*
