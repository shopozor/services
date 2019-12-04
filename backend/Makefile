ifndef API_PORT
	API_PORT=8080
endif

HASURA_ENDPOINT = http://localhost:${API_PORT}
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_MIGRATE_STATUS = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = ../shared/fixtures
GRAPHQL_RESPONSES_FOLDER = ../shared/graphql/responses

dev.start: build up db.migrate.up fixtures

dev.end: fixtures.clean down rm

build:
	@echo "Building images..."
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml build

up:
	@docker-compose -f docker-compose.yaml up -d postgres graphql-engine
	@chmod u+x ./database-service/scripts/waitForService.sh
	@./database-service/scripts/waitForService.sh localhost ${API_PORT}

down:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml down --remove-orphans

rm:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml rm -f

db.migrate.up:
	$(HASURA_MIGRATE_APPLY) --project database-service --skip-update-check

db.migrate.down:
	# TODO: this doesn't work!
	$(HASURA_MIGRATE_APPLY) --project database-service --down all --skip-update-check

db.migrate.status:
	$(HASURA_MIGRATE_STATUS) --project database-service --skip-update-check

fixtures.generate:
	@echo "Generating fixtures ..."
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up fixtures-service
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml rm -f fixtures-service

fixtures.up:
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database/small --up all --skip-update-check

fixtures.down: db.migrate.down

fixtures.clean:
	rm -rf $(FIXTURES_FOLDER)
	rm -rf $(GRAPHQL_RESPONSES_FOLDER)

fixtures: fixtures.clean fixtures.generate fixtures.up

test.database-service:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit hasura-service-tests

test.behave:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit features-tests

test: test.database-service

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	hasura console --project database-service

%.logs:
	docker-compose logs -f $*
