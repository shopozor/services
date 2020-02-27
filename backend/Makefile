fixtures.generate:
	@echo "Generating fixtures ..."
	@docker-compose -f ../docker-compose.yaml up fixtures-service
	@docker-compose -f ../docker-compose.yaml rm -f fixtures-service

test:
	@docker-compose -f ../docker-compose.yaml up --abort-on-container-exit database-service-tests
	@docker-compose -f ../docker-compose.yaml up --abort-on-container-exit service-integration-tests
