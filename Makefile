bootstrap:
	@yarn
	@yarn bootstrap

%:
	make --directory backend $*
	make --directory frontend $*

lint:
	@./scripts/check_linting.sh

dev.backend.start:
	@make --directory backend dev.start

dev.backend.end:
	@make --directory backend dev.end
