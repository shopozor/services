
HASURA_ENDPOINT = http://localhost:8080
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_STATUS_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
FIXTURES_FOLDER = database-service/fixtures
FIXTURES_MIGRATIONS_FOLDER = $(FIXTURES_FOLDER)/migrations

dev.start: up fixtures

dev.end: down fixtures.clean

up:
	@echo "Starting containers..."
	@docker-compose up -d
	@echo "Waiting for postgres to be ready for loading migrations..."
	@until make db.migrate.apply 2>&1 /dev/null; do echo "Waiting for database to be ready ..."; sleep 2s; done


down:
	@docker-compose down

db.migrate.apply:
	cd database-service && $(HASURA_MIGRATE_APPLY)

db.migrate.status:
	cd database-service && $(HASURA_MIGRATE_STATUS)

fixtures.generate:
	@echo "Generating fixtures ..."
	# without file config.yaml (even empty), hasura migrate apply will fail
	@if [ ! -d $(FIXTURES_MIGRATIONS_FOLDER) ]; then mkdir -p $(FIXTURES_MIGRATIONS_FOLDER); touch $(FIXTURES_FOLDER)/config.yaml; fi
	@docker-compose -f docker-compose-tests.yaml up fixtures-service
	@docker-compose -f docker-compose-tests.yaml rm -f fixtures-service


fixtures.up:
	cd $(FIXTURES_FOLDER) && $(HASURA_MIGRATE_APPLY) --up all

fixtures.down:
	cd $(FIXTURES_FOLDER && $(HASURA_MIGRATE_APPLY) --down all

fixtures.clean:
	rm -rf $(FIXTURES_MIGRATIONS_FOLDER)/*

fixtures: fixtures.clean fixtures.generate fixtures.up


%.restart:
	make $*.down
	make $*.up

logs:
	docker-compose logs -f

console:
	cd database-service && hasura console


%.logs:
	docker-compose logs -f $*
