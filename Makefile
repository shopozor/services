bootstrap:
	@yarn
	@yarn bootstrap

%:
	make --directory backend $*
	make --directory frontend $*

dev.backend.start:
	@make --directory backend dev.start

dev.backend.end:
	@make --directory backend dev.end