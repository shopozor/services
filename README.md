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
It will essentially run all the tests before pushing. You can then disable that with the following command:
```
pre-commit uninstall --hook-type pre-push
```

### VSCode configuration

Make sure you run the script
```
.vscode/install-extensions.sh
```

### Docker and docker-compose

Most of the backend stuff and the whole frontend validation are performed on docker containers:

* on Ubuntu, follow [these instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/)  
* on Windows 10, follow [these instructions](https://docs.docker.com/docker-for-windows/install/) and make sure you read [this blog](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly) if you work with WSL

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

### Lauching hasura console

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

### Necessary third-party packages

You will need to have `yarn` and `nodejs` installed:
```bash
curl -sL https://deb.nodesource.com/setup_10.x | bash -
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
apt update
apt install -y yarn nodejs
```
In addition, install [lerna](https://lerna.js.org/) globally
```bash
yarn global add lerna
```
Bootstrap the node projects
```bash
lerna bootstrap
```
and build them
```bash
lerna run build
```

### Troubleshooting

#### Ui unit tests

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
