bootstrap:
	@yarn
	@yarn bootstrap

%:
	make --directory backend $*
	make --directory frontend $*