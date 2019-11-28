#! /bin/bash

ln -s /home/node/node_modules/ node_modules 
yarn cypress:integration:ci 
EXIT_CODE=$?
rm -f node_modules

exit ${EXIT_CODE}
