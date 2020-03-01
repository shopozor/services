bootstrap:
	@yarn
	@yarn bootstrap

down:
	@docker-compose down --remove-orphans
