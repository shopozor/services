#! /bin/bash

ln -s /home/node/node_modules/ node_modules 
yarn test:unit:ci 
rm -f node_modules