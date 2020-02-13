#! /bin/sh

WORKDIR=$PWD
cd ${SRC_DIR} && yarn generate
cd ${WORKDIR} && yarn start