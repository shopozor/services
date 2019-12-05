#! /bin/bash

for f in `find . -name "*.sh"` ; do
  git update-index --chmod=+x $f
done