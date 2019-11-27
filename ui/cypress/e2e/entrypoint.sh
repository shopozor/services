#! /bin/bash

ln -s /home/node/node_modules/ node_modules 
yarn cypress:e2e:ci 
rm -f node_modules