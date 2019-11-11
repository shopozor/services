HASURA_ENDPOINT = http://localhost:8080
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_STATUS_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = ./fixtures
FIXTURES_MIGRATIONS_FOLDER = $(FIXTURES_FOLDER)/migrations

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
	@docker-compose -f docker-compose-tests.yaml down

rm:
	@docker-compose rm -f
	@docker-compose -f docker-compose-tests.yaml rm -f


db.migrate.apply:
	$(HASURA_MIGRATE_APPLY) --project database-service

db.migrate.status:
	$(HASURA_MIGRATE_STATUS) --project database-service

fixtures.generate:
	@echo "Generating fixtures ..."
	@if [ -d fixtures ]; then rm -rf $(FIXTURES_FOLDER); fi
	@mkdir $(FIXTURES_FOLDER)
	@docker-compose -f docker-compose-tests.yaml -f docker-compose-tests-dev.yaml up fixtures-service
	@docker-compose -f docker-compose-tests.yaml rm -f fixtures-service

fixtures.up:
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER) --up all

fixtures.down:
	# TODO: get the number of migrations from a truncated $(shell echo $((`ls database-service/migrations | wc -l`/2)))
	$(HASURA_MIGRATE_APPLY) --project $(FIXTURES_FOLDER) --down 6

fixtures.clean:
	rm -rf $(FIXTURES_MIGRATIONS_FOLDER)/*

fixtures: fixtures.clean fixtures.generate fixtures.up

test:
	@docker-compose -f docker-compose-tests.yaml up --abort-on-container-exit postgres graphql-engine hasura-service-tests
	@docker-compose down

%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	cd database-service && hasura console

%.logs:
	docker-compose logs -f $*
