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

dev-test.admin-unit:
	@lerna run test:unit --scope admin-ui --stream

dev-test.consumer-unit:
	@lerna run test:unit --scope consumer-ui --stream

dev-test.admin-integration:
	@lerna run cypress:integration:dev --scope admin-ui --stream

dev-test.consumer-integration:
	@lerna run cypress:integration:dev --scope consumer-ui --stream

dev-test.integration:
	@lerna run cypress:integration:dev --stream --concurrency 1

dev-test.admin-e2e:
  # TODO: find a solution for this GRAPHQL_API variable; at least define it from an env variable
	@GRAPHQL_API=http://localhost:8080/v1/graphql lerna run cypress:e2e:dev --scope admin-ui --stream

dev-test.consumer-e2e:
	@lerna run cypress:e2e:dev --scope consumer-ui --stream

dev-test.e2e:
  # TODO: find a solution for this GRAPHQL_API variable; at least define it from an env variable
	@GRAPHQL_API=http://localhost:8080/v1/graphql lerna run cypress:e2e:dev --stream --concurrency 1

up:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml up -d consumer-ui admin-ui

build:
	@echo "Building images..."
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml build

down:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml down --remove-orphans

rm:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml rm -f

test.integration:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml up --abort-on-container-exit consumer-storybook admin-storybook ui-integration-tests

test.e2e:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-frontend.yaml -f ../docker-compose-frontend-tests.yaml up --abort-on-container-exit consumer-ui admin-ui e2e-tests

test.cleanup: down rm

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

%.logs:
	docker-compose logs -f $*
