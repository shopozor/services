[![Tests Build Status](http://shopozor-ci.hidora.com/buildStatus/icon?job=tests-pr&subject=tests)](http://shopozor-ci.hidora.com/job/tests-pr/)

# Introduction

In the past, we made evaluations on many existing open source software that we could wrap and use as our backend. Our last attempts were with [vuestorefront](https://www.vuestorefront.io/) and [saleor](https://getsaleor.com/). The latter was the most developped of our attempts. It was almost sure that it would be our production backend.

However, `saleor` is written in python and builds up its graphql API with graphene. That has the following disadvantages:

- very slow graphql API calls
- very slow unit tests
- very slow integration / functional tests
- impossible to load a set of fixtures before all acceptance scenarios and only revert the changes made within a single acceptance scenario
- difficult to make subscriptions happen
- difficult with Django to make safe accesses to the postgres database; by default, `saleor` defines one single database user with all the necessary permissions, which is dangerous; it would be better to use the built-in postgres views to restrict the database users' permissions based on the purpose they have
- `saleor` is a big monolith where views are entangled with logic; for example, it would be a lot of work to only take the pure logic out of it; one smell of that is the way their unit tests are organized: it is a lot of work to unbraid view tests from logic tests and it is also a lot of work to unbraid their module dependencies

## Useful dev links

* [Quasar testing](https://testing.quasar.dev/)
* [GraphQL Vue Tutorial](https://learn.hasura.io/graphql/vue/introduction)
* [Vue testing handbook](https://lmiller1990.github.io/vue-testing-handbook/)
* Testing Vue.js applications in our google drive
* [Get started with storybook](https://medium.com/@mtiller/testing-react-components-using-storybook-and-cypress-1689a27f55aa)
* [Storybook for Vue](https://storybook.js.org/docs/guides/guide-vue/)
* [Storybook and Cypress](https://medium.com/@mtiller/testing-react-components-using-storybook-and-cypress-1689a27f55aa)
* [Nuxt and apollo link state](https://www.meidev.co/blog/nuxt-and-apollo-link-state/)
* [Local state management with apollo](https://vue-apollo.netlify.com/guide/local-state.html#why-use-apollo-local-state-management)

# Development setup

## General setup

### Pre-commit hooks

The first time you clone this repo, you need to configure `pre-commit` hooks:
```
apt install -y python3-pip
pip install pre-commit
git clone https://github.com/shopozor/services
cd services
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template
```
After that, everytime you will clone a new git repository, the `pre-commit` hooks will be enforced automatically. Would you like to enable pre-push hooks, you'd need to also run the following command in the `services` root folder:
```
pre-commit install --hook-type pre-push
```
It will essentially run all the tests before pushing. You can then disable pre-push hooks with the following command:
```
pre-commit uninstall --hook-type pre-push
```
Note that the pre-push hooks will not work on git bash under Windows. Under Windows, you will need to work with WSL to let that happen.

### VSCode configuration

Make sure you run the script
```
.vscode/install-extensions.sh
```

### Docker and docker-compose

Most of the backend stuff and the whole frontend validation are performed on docker containers:

* on Ubuntu, follow [these instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/)  
* on Windows 10, follow [these instructions](https://docs.docker.com/docker-for-windows/install/) and make sure you read [this blog](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly) if you work with WSL

Do not use Docker for Desktop 2.2.0.0. It is not working. The last working stable version is, as far as we know, version 2.1.0.5.

### Kubernetes

Under linux, install minikube. Under Windows, you can enable kubernetes in Docker Desktop:

![k8s settings in docker desktop](doc/img/enable_k8s.png)

You will want to

* [install helm](https://helm.sh/docs/intro/install/) too, e.g. with [chocolatey](https://chocolatey.org/packages/kubernetes-helm) under Windows.
* install the kubernetes dashboard, following [this advice](https://collabnix.com/kubernetes-dashboard-on-docker-desktop-for-windows-2-0-0-3-in-2-minutes/) and [this documentation](https://github.com/kubernetes/dashboard)
* [install skaffold](https://skaffold.dev/docs/install/)
* [activate the helm charts repo](https://github.com/helm/charts#how-do-i-enable-the-stable-repository-for-helm-3)
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo add bitnami https://charts.bitnami.com/bitnami
```
* [install squash](https://squash.solo.io/overview/) in order to be able to debug your k8s app

#### Kubernetes dashboard

Once installed, you access the k8s dashboard as follows:

1. run
```
kubectl proxy
``
2. using your favorite browser, navigate to

http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

3. on that address, you will need to provide a token; you find it in the following way (under Windows with default kubernetes installation through the docker for desktop):
```
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep default-token | awk '{print $1}')
```

### Common third-party packages

In order to play with the assets, you will probably need the [minio client](https://docs.min.io/docs/minio-client-quickstart-guide.html). Under Windows 10,

1. download the [client](https://dl.min.io/client/mc/release/windows-amd64/mc.exe)
2. run
```
export MINIO_ACCESS_KEY=minio
export MINIO_SECRET_KEY=minio123
export MINIO_PORT=9001
mc config host add minio http://localhost:${MINIO_PORT} ${MINIO_ACCESS_KEY} ${MINIO_SECRET_KEY}
```
Compare with the data set up in the `docker-compose-backend.yaml`. The `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, and the `MINIO_PORT` might be different in your local setup. Some more information here on how to use [min.io](https://min.io) in our frontend applications:

* [minio js store app](https://github.com/minio/minio-js-store-app)
* [Get permanent URL for object](https://github.com/minio/minio-js/issues/588)
* [Javascript Client API reference](https://docs.min.io/docs/javascript-client-api-reference.html)
* [minio client quickstart guide](https://docs.min.io/docs/minio-client-quickstart-guide.html)

## Backend development setup

### Necessary third-party packages

Some of our scripts use the `jq` tool to interpret json output. Under ubuntu / debian, you will need `jq`:
```
sudo apt install -y jq
```
Under Windows 10, you want to install [jq](https://github.com/stedolan/jq/releases). Just download the Win64 installer and make it available somewhere in your disk. Add that location to your `PATH` variable. Rename `jq-win64.exe` to `jq.exe`.

### Development database seeding

To start development environment, just enter following command that will take
care of everything, including applying migrations and loading fixtures

```bash
make dev.start
```

This command handles the case where the `graphql-engine` cannot connect to the `postgres` service for a moment and retries to apply migrations until it works. Therefore, this command can take up to 30 seconds to be successful. Just ignore the error messages on the console.

### Development database tear-down

When you are over with development (or when you checkout another branch) and
want your environment to be clean, just do

```bash
make dev.end
```

### Launching hasura console

To launch console, which is the only way to automatically generate the corresponding hasura migrations, enter following command from the root of the repo

```bash
make console
```

### Starting the database and applying migrations

Special rules in the `Makefile` take care of setting up everything for
development. To start Hasura and PostgreSQL and apply the migrations, just run

```bash
make up
```

This command will probably output error messages due to the postgres DB not
being ready for loading the fixtures.

```
FATA[0001] version check: failed to get version from server: failed making version api call: Get http://localhost:8080/v1/version: EOF
Makefile:18: recipe for target 'db.migrate.apply' failed
make[1]: *** [db.migrate.apply] Error 1
make[1]: Leaving directory '/c/Users/cedon/linux/softozor/backend'
Waiting for database to be ready ...
make[1]: Entering directory '/c/Users/cedon/linux/softozor/backend'
cd database-service && hasura migrate apply --endpoint http://localhost:8080
INFO migrations applied
```

Just wait until the migrations are applied.

### Generating fixtures and loading them into the database

Just run the following command at the root of this repo

```bash
make fixtures
```

## Frontend development setup

### Caution notice

**Never ever** remove any `yarn.lock` file, if you don't want to lose your time fixing the build.

### Necessary third-party packages

You will need to have `yarn` and `nodejs` installed. Under WSL or Linux, you can run the following commands (or you can also follow [this advice](https://askubuntu.com/questions/426750/how-can-i-update-my-nodejs-to-the-latest-version)):
```bash
curl -sL https://deb.nodesource.com/setup_10.x | bash -
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
apt update
apt install -y yarn nodejs
```
If you're not using WSL because `yarn` is still buggy there, you should then [install nodejs](https://nodejs.org/) and [install yarn](https://yarnpkg.com/en/docs/install#windows-stable).

In addition, install [lerna](https://lerna.js.org/) globally
```bash
yarn global add lerna
```
That tool simplifies management of monorepos. While not strictly necessary in the global environment of our build systems, it's pretty handy to have it globally available on development environments.

Finally, bootstrap the node packages like this:
```bash
make bootstrap
```

### Starting the frontends

For the sake of development, you will almost never need to **build** the frontends. Building the frontends will be done for you in the testing commands.

To start the frontends in development mode, just run
```bash
yarn start:dev
```
at the root of this monorepo. To only start one of the frontends, run the previous command with the `--scope` option:
```bash
yarn start:dev --scope consumer-ui
yarn start:dev --scope admin-ui
```

### Storybook

[Storybook](storybook.js.org) is a very nice tool allowing devs to develop their components in an isolated environment. You can start storybook the very same way you start the frontends:
```bash
yarn storybook
```
or
```bash
yarn storybook --scope consumer-ui
yarn storybook --scope admin-ui
```
Not only is storybook nice to develop components isolately, it's aslo providing us with out-of-the-box snapshot testing of each of those components. It can be that we have e.g. very simple components like a header or a footer with almost no logic. That component's snapshot will, however, be tested.

### Testing

We defined several kinds of UI tests. We have the unit and integration tests. Unit tests cover both isolated component tests as well as snapshot tests (essentially defined by storybook). Testing is not run exactly the same way on development as on continuous integration environments. On the latter, we run the tests in docker images. On the former, we just run them directly on the development system's OS.

#### Unit tests

In the `frontend` folder, run either one of the following commands, depending on what you want to test:
```bash
# Only the admin-ui unit tests
make dev-test.admin-unit
# Only the consumer-ui unit tests
make dev-test.consumer-unit
# All the frontend unit tests
make dev-test.unit
```

#### Integration tests

It's not crystal clear if we really want to have integration tests for our UIs. An integration test would typically use a few components and test their interactions. That would be done within storybook where we would define stories that put those components together. With Cypress, we would then browse the corresponding story and perform the necessary tests. No such test has been defined yet. The necessary code infrastructure is however already in place. To run the initial, dummy integration tests, run the following commands in the `frontend` folder:
```bash
make dev-test.admin-integration
make dev-test.consumer-integration
make dev-test.integration
```

## Testing the whole stack

Before pushing your changes to the git server, you may want to check that you broke nothing. You can do that by enabling the corresponding pre-push hook as explained above. In that case, however, it'll be difficult to use your IDE's built-in commands to push your code, which might be annoying. Another way is to just run the tests manually like follows, in the repository's root:
```bash
make dev-test.all
```
Feel free to have a look at the `Makefile`s to see what happens under the hood. You will discover how to run the whole backend or the whole frontend tests separately too:
```bash
make dev-test.run-backend
make dev-test.run-frontend
```
Indeed, if you only changed code on the frontend side, you probably don't want to spend your time testing the backend.

### End-to-end tests

The end-to-end tests are run by command
```bash
make dev-test.run-frontend
```
Those tests ensure that the whole application flow is working as expected. They need database data. To run them without running the other tests, you need to generate the fixtures, run the backend, seed the database, and then run the e2e tests:
```bash
make --directory backend fixtures.generate
make --directory backend up
make --directory backend seed-database
make --directory frontend dev-test.e2e
```
Instead of the last line, you might want to only run the e2e tests of one frontend at a time, which you do like this:
```bash
make --directory frontend dev-test.admin-e2e
make --directory frontend dev-test.consumer-e2e
```

## Troubleshooting

### The database is not reset

It might be that you've followed this introduction and run all the services, tests, etc. Then you rebooted your PC and re-run the stuff and ... ooops, I can't seed the database anymore! Beacuse we develop a lot of features all the time, the fixtures set also evolves a lot and might need to be applied several times a week (or a day). Once the fixtures set has been applied to the database, you can't apply a new one, because the data already exist. When you're done testing, make sure you run in the repository's root
```bash
make down
```
That shuts down all the backend services. In particular, that shuts down the database. Next time you run the backend, the database will be empty and you can apply the fixtures again.

### Ui unit tests

Upon running the ui unit tests, you might get an error of the kind (especially on Windows machines):
```
Cannot find module '[..]/ui/node_modules/@quasar/babel-preset-app/node_modules/@babel/runtime/helpers/interopRequireDefault' from 'jest.setup.js'
```
Following [this advice](https://forum.quasar-framework.org/topic/3760/fix-babel-error-after-update-from-v1-0-0-beta22-to-v1-0-0-rc4), you can fix it this way:
```
cd node_modules/@quasar/babel-preset-app && yarn
```

## Specification generation

### Gherkin step skeletons

It is pretty handy to get the skeleton code for each step of a feature file. That can be reached with the following command for the `LogAUserIn` feature
```
cd ui/cypress/integration/Authentication
npx cucumber-js LogAUserIn.feature
```
which outputs for example
```
1) Scenario: Le membre du staff n'est pas encore enregistré # LogAUserIn.feature:13
   ? Etant donné un utilisateur non identifié
       Undefined. Implement with the following snippet:

         Given('un utilisateur non identifié', function () {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });

   ? Lorsqu'un utilisateur s'identifie avec un e-mail et un mot de passe invalides
       Undefined. Implement with the following snippet:

         When('un utilisateur s\'identifie avec un e-mail et un mot de passe invalides', function () {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });

   ? Alors il obtient un message d'erreur stipulant que ses identifiants sont incorrects
       Undefined. Implement with the following snippet:

         Then('il obtient un message d\'erreur stipulant que ses identifiants sont incorrects', function () {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });
```

## CI / CD

Useful documentation on how to work with helm can be found here:

* [create your first helm chart](https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/)
* [helm quickstart guide](https://helm.sh/docs/intro/quickstart/)
* [helmfile](https://github.com/roboll/helmfile)
* [dry k8s with helm](https://blog.mimacom.com/dry-kubernetes-with-helm/)
* [microservices deployment with helm and skaffold](https://github.com/GoogleCloudPlatform/microservices-demo/blob/master/skaffold.yaml)
* [example deployment with helm and skaffold](https://github.com/cmcornejocrespo/auvik-helm-skaffold/blob/master/skaffold.yaml)
* [draft vs skaffold vs garden](https://codefresh.io/howtos/local-k8s-draft-skaffold-garden/)
* [monorepo cicd helm k8s](https://www.infracloud.io/monorepo-ci-cd-helm-kubernetes/)
* [gitlab monorepo pipelines](https://aarongorka.com/blog/gitlab-monorepo-pipelines/)

In essence, our CI/CD process amounts to (see [microsoft documentation](https://docs.microsoft.com/en-us/azure/architecture/microservices/ci-cd-kubernetes))

![overall ci / cd process](doc/img/cicd.png)