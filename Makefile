HASURA_ENDPOINT = http://localhost:${API_PORT}
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_STATUS_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = ./fixtures
GRAPHQL_RESPONSES_FOLDER = ./graphql/responses

dev.start: build up db.migrate.apply fixtures

dev.end: down fixtures.clean rm

build:
	@echo "Building images..."
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml build

up:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up -d postgres graphql-engine ui
	@chmod u+x ./database-service/scripts/waitForService.sh
	./database-service/scripts/waitForService.sh localhost ${API_PORT}

down:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml down

rm:
	@docker-compose rm -f
	@docker-compose -f docker-compose-tests.yaml rm -f

db.migrate.apply:
	$(HASURA_MIGRATE_APPLY) --project database-service --skip-update-check

db.migrate.status:
	$(HASURA_MIGRATE_STATUS) --project database-service --skip-update-check

fixtures.generate:
	@echo "Generating fixtures ..."
	@chmod u+x ./fixtures-generator/entrypoint.sh
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml -f docker-compose-tests-dev.yaml up fixtures-service
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml rm -f fixtures-service

fixtures.up:
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER) --up all --skip-update-check

fixtures.down:
	# TODO: get the number of migrations from a truncated $(shell echo $((`ls database-service/migrations | wc -l`/2)))
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER) --down 6 --skip-update-check

fixtures.clean:
	rm -rf $(FIXTURES_FOLDER)
	rm -rf $(GRAPHQL_RESPONSES_FOLDER)

fixtures: fixtures.clean fixtures.generate fixtures.up

test.database-service:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit hasura-service-tests

test.ui-unit-tests:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit ui-unit-tests

test.ui-integration-tests:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit ui-integration-tests

test.e2e-tests:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit e2e-tests

test.behave:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit features-tests

test: test.database-service test.ui-unit-test test.ui-integration-tests test.e2e-tests

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	hasura console --project database-service 

%.logs:
	docker-compose logs -f $*
