dev.start.admin: init dev.backend.start
	@lerna run start:dev --scope admin-ui

dev.start.consumer: init dev.backend.start
	@lerna run start:dev --scope consumer-ui

dev.start.all: init dev.backend.start
	@lerna run start:dev

init:
	@make --directory .. dev.start

dev.end: dev.backend.end

dev.backend.start:
	@make --directory ../backend dev.start

dev.backend.end:
	@make --directory ../backend dev.end

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

build:
	@echo "Building images..."
	@docker-compose -f ../backend/docker-compose.yaml -f docker-compose.yaml -f docker-compose-tests.yaml build

# up: admin-ui.up consumer-ui.up

down:
	@docker-compose -f ../backend/docker-compose.yaml -f docker-compose.yaml -f docker-compose-tests.yaml down --remove-orphans

rm:
	@docker-compose -f ../backend/docker-compose.yaml -f docker-compose.yaml -f docker-compose-tests.yaml rm -f

test.ui-unit:
	@docker-compose -f ../backend/docker-compose.yaml -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit ui-unit-tests

test.ui-integration:
	@docker-compose -f ../backend/docker-compose.yaml -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit ui-integration-tests

test.e2e:
	@docker-compose -f ../backend/docker-compose.yaml -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit e2e-tests

test: build test.ui-unit test.ui-integration test.e2e
test.cleanup: down rm

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

%.logs:
	docker-compose logs -f $*
