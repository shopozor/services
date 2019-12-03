#! /bin/bash

for app in admin-ui consumer-ui ; do
  cd /app/frontend/$app
  CYPRESS_baseUrl="http://$app:4000/#" cypress run --env configFile=integration
done