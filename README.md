# Shopozor micro-services

## Build statuses

[![Tests Build Status](http://shopozor-ci.hidora.com/buildStatus/icon?job=tests-pr&subject=tests)](http://shopozor-ci.hidora.com/job/tests-pr/)

## Introduction

In the past, we made evaluations on many existing open source software that we could wrap and use as our backend. Our last attempts were with [vuestorefront](https://www.vuestorefront.io/) and [saleor](https://getsaleor.com/). The latter was the most developped of our attempts. It was almost sure that it would be our production backend.

However, `saleor` is written in python and builds up its graphql API with graphene. That has the following disadvantages:

- very slow graphql API calls
- very slow unit tests
- very slow integration / functional tests
- impossible to load a set of fixtures before all acceptance scenarios and only revert the changes made within a single acceptance scenario
- difficult to make subscriptions happen
- difficult with Django to make safe accesses to the postgres database; by default, `saleor` defines one single database user with all the necessary permissions, which is dangerous; it would be better to use the built-in postgres views to restrict the database users' permissions based on the purpose they have
- `saleor` is a big monolith where views are entangled with logic; for example, it would be a lot of work to only take the pure logic out of it; one smell of that is the way their unit tests are organized: it is a lot of work to unbraid view tests from logic tests and it is also a lot of work to unbraid their module dependencies

## Development setup

### Useful links

* [Quasar testing](https://testing.quasar.dev/)
* [Vue testing handbook](https://lmiller1990.github.io/vue-testing-handbook/)
* Testing Vue.js applications in our google drive

### Pre-commit hooks

As it is not trivial to enforce automatic installation of the pre-commit hooks, just install them yourself:

```
pre-commit install
```

That pre-supposes that you have the `pre-commit` module installed in your python
environment.

### VSCode configuration

Make sure you run the script
```
.vscode/install-extensions.sh
```

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

### Setting everything up for development

To start development environment, just enter following command that will take
care of everything, including applying migrations and loading fixtures

```bash
make dev.start
```

This command handles the case where the `graphql-engine` cannot connect to the `postgres` service for a moment and retries to apply migrations until it works. Therefore, this command can take up to 30 seconds to be successful. Just ignore the error messages on the console.

### Tearing everything down when development is finished

When you are over with development (or when you checkout another branch) and
want your environment to be clean, just do

```bash
make dev.stop
```

### Lauching console

To launch console, enter following command from the root of the repo

```bash
make console
```

## More fine-grained control ...

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

### Generating fixtures and loading them into the BD

Just run the following command at the root of this repo

```bash
make fixtures
```

## Running tests

To run the tests, use the command

```bash
$ make test
```

To run acceptance tests, use the command

```
$ make test.behave
```

## Troubleshooting

### Ui unit tests

Upon running the ui unit tests, you might get an error of the kind (especially on Windows machines):
```
Cannot find module '[..]/ui/node_modules/@quasar/babel-preset-app/node_modules/@babel/runtime/helpers/interopRequireDefault' from 'jest.setup.js'
```
Following [this advice](https://forum.quasar-framework.org/topic/3760/fix-babel-error-after-update-from-v1-0-0-beta22-to-v1-0-0-rc4), you can fix it this way:
```
cd node_modules/@quasar/babel-preset-app && yarn
```
