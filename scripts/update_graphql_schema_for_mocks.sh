#! /bin/bash

ENDPOINT=${1:-http://api.shopozor/v1/graphql}

npx gq $ENDPOINT --introspect > schema.graphql

sed -i 's/query_root/Query/g' schema.graphql
sed -i 's/mutation_root/Mutation/g' schema.graphql
sed -i 's/subscription_root/Subscription/g' schema.graphql

cp schema.graphql frontend/consumer-ui/.storybook/schema/schema.graphql
cp schema.graphql frontend/admin-ui/.storybook/schema/schema.graphql

rm schema.graphql