#! /bin/bash

ln -s /home/node/node_modules/ node_modules 
yarn cypress:integration:ci 
rm -f node_modules