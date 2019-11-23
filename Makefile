HASURA_ENDPOINT = http://localhost:8080
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_STATUS_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = ./fixtures

dev.start: up fixtures

dev.end: down fixtures.clean rm

build:
	@echo "Building images..."
	@docker-compose build
	@docker-compose -f docker-compose-tests.yaml build

up: build
	@echo "Starting containers..."
	@docker-compose up -d postgres
	@sleep 1s
	@docker-compose up -d graphql-engine
	@echo "Waiting for postgres to be ready for loading migrations..."
	@until make db.migrate.apply 2>&1 /dev/null; do echo "Waiting for database to be ready ..."; sleep 2s; done

down:
	@docker-compose down
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml down

rm:
	@docker-compose rm -f
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml rm -f


db.migrate.apply:
	$(HASURA_MIGRATE_APPLY) --project database-service --skip-update-check

db.migrate.status:
	$(HASURA_MIGRATE_STATUS) --project database-service --skip-update-check

fixtures.generate:
	@echo "Generating fixtures ..."
	@if [ -d $(FIXTURES_FOLDER) ]; then rm -rf $(FIXTURES_FOLDER); fi
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml -f docker-compose-tests-dev.yaml up fixtures-service
	@docker-compose -f docker-compose.yaml rm -f fixtures-service

fixtures.up:
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database/small --up all --skip-update-check

fixtures.down:
	# TODO: get the number of migrations from a truncated $(shell echo $((`ls database-service/migrations | wc -l`/2)))
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER)/database/small --down 6 --skip-update-check

fixtures.clean:
	rm -rf $(FIXTURES_FOLDER)

fixtures: fixtures.clean fixtures.generate fixtures.up

test:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit postgres graphql-engine hasura-service-tests
	@docker-compose down

test.behave:
	@docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit features-tests

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	cd database-service && hasura console

%.logs:
	docker-compose logs -f $*
