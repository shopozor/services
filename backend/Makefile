ifndef API_PORT
	API_PORT=8080
endif

ifndef MINIO_PORT
	MINIO_PORT=9001
endif

HASURA_ENDPOINT = http://localhost:${API_PORT}
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_MIGRATE_STATUS = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = ../shared/fixtures
GRAPHQL_RESPONSES_FOLDER = ../shared/graphql/responses

dev.start: build up db.migrate.up fixtures assets.up

dev.end: fixtures.clean assets.down down rm

dev-test.site-generator-unit:
	@npx lerna run test:unit --scope site-generator-service --stream

build:
	@echo "Building images..."
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml build

up:
	@docker-compose -f ../docker-compose-backend.yaml up -d minio-setup postgres graphql-engine site-generator-service
	@./database-service/scripts/waitForService.sh localhost ${API_PORT}

down:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml down --remove-orphans

rm:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml rm -f

static-site.generate:
	@docker-compose -f ../docker-compose-backend.yaml up generate-site-job

assets.up:
	@./assets-service/scripts/push_fixtures.sh

assets.down:
	@./assets-service/scripts/cleanup_fixtures.sh

db.migrate.up:
	$(HASURA_MIGRATE_APPLY) --project database-service --skip-update-check

db.migrate.down:
	# This will only work as long as we don't switch to folder structure
	@$(HASURA_MIGRATE_APPLY) --project database-service --down $(shell ls database-service/migrations/*.up.yaml | wc -l) --skip-update-check

db.migrate.status:
	@$(HASURA_MIGRATE_STATUS) --project database-service --skip-update-check

fixtures.generate:
	@echo "Generating fixtures ..."
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml up fixtures-service
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml rm -f fixtures-service

fixtures.up:
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database --up all --skip-update-check

fixtures.down:
	# This will only work as long as we don't switch to folder structure
	@$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database --down $(shell ls $(FIXTURES_FOLDER)/database/migrations/*.up.sql | wc -l) --skip-update-check

fixtures.clean:
	rm -rf $(FIXTURES_FOLDER)
	rm -rf $(GRAPHQL_RESPONSES_FOLDER)

fixtures: fixtures.clean fixtures.generate fixtures.up

seed-database: db.migrate.up fixtures.up
unseed-database: fixtures.down db.migrate.down

test.database-service:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml up --abort-on-container-exit database-service-tests

test.integration:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml up --abort-on-container-exit service-integration-tests

test.behave:
	@docker-compose -f ../docker-compose-backend.yaml -f ../docker-compose-backend-tests.yaml up --abort-on-container-exit features-tests

test.unit: test.database-service
test: test.unit test.integration

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	hasura console --project database-service

%.logs:
	docker-compose logs -f $*