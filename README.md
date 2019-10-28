# Backend micro-services

## Introduction

In the past, we made evaluations on many existing open source software that we could wrap and use as our backend. Our last attempts were with [vuestorefront](https://www.vuestorefront.io/) and [saleor](https://getsaleor.com/). The latter was the most developped of our attempts. It was almost sure that it would be our production backend.

However, `saleor` is written in python and builds up its graphql API with graphene. That has the following disadvantages:

* very slow graphql API calls
* very slow unit tests
* very slow integration / functional tests
* impossible to load a set of fixtures before all acceptance scenarios and only revert the changes made within a single acceptance scenario
* difficult to make subscriptions happen
* difficult with Django to make safe accesses to the postgres database; by default, `saleor` defines one single database user with all the necessary permissions, which is dangerous; it would be better to use the built-in postgres views to restrict the database users' permissions based on the purpose they have
* `saleor` is a big monolith where views are entangled with logic; for example, it would be a lot of work to only take the pure logic out of it; one smell of that is the way their unit tests are organized: it is a lot of work to unbraid view tests from logic tests and it is also a lot of work to unbraid their module dependencies

## Development setup

### Pre-commit hooks

As it is not trivial to enforce automatic installation of the pre-commit hooks, just install them yourself:
```
pre-commit install
```
That pre-supposes that you have the `pre-commit` module installed in your python environment.