#!/bin/sh

if [ ! -z "$1" ] && [ "$1" -eq "$1" ]; then
  howmany=`expr $1 + 1`
else
  howmany="10"
fi

count=1
while [ $count -lt $howmany ]
do
echo "Image $count"
curl https://i.picsum.photos/id/$(shuf -i 0-1000 -n 1)/300/300.jpg \
  -o "shop_$count.jpg"
  sleep 2s
  count=`expr $count + 1`
done