bootstrap:
	@yarn
	@yarn bootstrap

%:
	make --directory backend $*
	make --directory frontend $*

lint:
	@./scripts/check_linting.sh