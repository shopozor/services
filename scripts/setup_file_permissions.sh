#! /bin/bash

for f in `find . -name "*.sh" -not -path "*node_modules*"` ; do
  git update-index --chmod=+x $f
done