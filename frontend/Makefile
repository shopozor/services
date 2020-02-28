# TODO: mount a docker container into the dev cluster where we can run the tests in the console!
dev-test.admin-unit:
	@npx lerna run test:unit --scope admin-ui --stream

dev-test.consumer-unit:
	@npx lerna run test:unit --scope consumer-ui --stream

dev-test.admin-e2e:
	@GRAPHQL_API=http://api.shopozor/v1/graphql npx lerna run cypress:e2e:dev --scope admin-ui --stream

dev-test.consumer-e2e:
	@npx lerna run cypress:e2e:dev --scope consumer-ui --stream

dev-test.e2e:
	@GRAPHQL_API=http://api.shopozor/v1/graphql npx lerna run cypress:e2e:dev --stream --concurrency 1

test.e2e:
	@docker-compose -f ../docker-compose.yaml up --abort-on-container-exit e2e-tests
