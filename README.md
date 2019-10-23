# Backend micro-services

## Introduction

In the past, we made evaluations on many existing open source software that we could wrap and use as our backend. Our last attempts were with `vue-storefront` and `saleor`. The latter was the most developped of our attempts. It was almost sure that it would be our production backend. 

However, `saleor` is written in python and builds up its graphql API with graphene. That has the following disadvantages:

* very slow graphql API calls
* very slow unit tests
* very slow integration / functional tests
* difficult to make subscriptions happen
* `saleor` is a big monolith where views are entangled with logic; for example, it would be a lot of work to only take the pure logic out of it; one smell of that is the way their unit tests are organized: it is a lot of work to unbraid view tests from logic tests and it is also a lot of work to unbraid their module dependencies