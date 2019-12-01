ifndef API_PORT
	API_PORT=8080
endif

HASURA_ENDPOINT = http://localhost:${API_PORT}
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_MIGRATE_STATUS = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = ./shared/fixtures
GRAPHQL_RESPONSES_FOLDER = ./shared/graphql/responses

dev.start: build up db.migrate.apply fixtures

dev.end: down fixtures.clean rm

ui.down:
ui.stop:
ui.restart:
ui.build:
ui.%:
	@echo "Do docker-compose $* of Admin UI image ..."
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml $* ui

ui.up: ui.build
	@echo "Do docker-compose $* of Admin UI image ..."
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml up -d ui

build:
	@echo "Building images..."
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-tests.yaml -f docker-compose-ui-tests.yaml build

up:
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml up -d postgres graphql-engine admin-ui
	@chmod u+x ./backend/database-service/scripts/waitForService.sh
	@./backend/database-service/scripts/waitForService.sh localhost ${API_PORT}

down:
	@docker-compose down --remove-orphans
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml down

rm:
	@docker-compose rm -f
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml rm -f

db.migrate.apply:
	$(HASURA_MIGRATE_APPLY) --project backend/database-service --skip-update-check

db.migrate.status:
	$(HASURA_MIGRATE_STATUS) --project backend/database-service --skip-update-check

fixtures.generate:
	@echo "Generating fixtures ..."
	@chmod u+x ./backend/fixtures-generator/entrypoint.sh
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up fixtures-service
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml rm -f fixtures-service

fixtures.up:
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database/small --up all --skip-update-check

fixtures.down:
	# TODO: get the number of migrations from a truncated $(shell echo $((`ls database-service/migrations | wc -l`/2)))
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database/small --down 6 --skip-update-check

fixtures.clean:
	rm -rf $(FIXTURES_FOLDER)
	rm -rf $(GRAPHQL_RESPONSES_FOLDER)

fixtures: fixtures.clean fixtures.generate fixtures.up

test.database-service:
	@chmod u+x ./backend/database-service/tests/entrypoint.sh
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit hasura-service-tests

test.ui-unit:
	@chmod u+x ./frontend/tests/entrypoint-unit.sh
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-ui-tests.yaml up --abort-on-container-exit ui-unit-tests

test.ui-integration:
	@chmod u+x ./frontend/tests/entrypoint-integration.sh
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-ui-tests.yaml up --abort-on-container-exit ui-integration-tests

test.e2e:
	@chmod u+x ./frontend/tests/entrypoint-e2e.sh
	@docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-ui-tests.yaml up --abort-on-container-exit e2e-tests

test.behave:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit features-tests

backend.test: test.database-service
ui.test: test.ui-unit test.ui-integration test.e2e
test: backend.test ui.test

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	hasura console --project backend/database-service

%.logs:
	docker-compose logs -f $*
