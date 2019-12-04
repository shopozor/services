bootstrap:
	@yarn
	@lerna bootstrap

%:
	make --directory backend $*
	make --directory frontend $*