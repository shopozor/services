
HASURA_ENDPOINT = http://localhost:8080
HASURA_MIGRATE_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)
HASURA_STATUS_APPLY = hasura migrate apply --endpoint $(HASURA_ENDPOINT)

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
	@if [ ! -d fixtures/migrations ]; then mkdir -p fixtures/migrations; fi
	@docker-compose -f docker-compose-tests.yaml up fixtures-service
	@docker-compose -f docker-compose-tests.yaml rm -f fixtures-service


fixtures.up:
	cd fixtures && $(HASURA_MIGRATE_APPLY) --up all

fixtures.down:
	cd fixtures && $(HASURA_MIGRATE_APPLY) --down all

fixtures.clean:
	rm -rf fixtures/migrations/*

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
