#!/bin/sh

if [ ! -z "$1" ] && [ "$1" -eq "$1" ]; then
  howmany=`expr $1 + 1`
else
  howmany="10"
fi

count=10
while [ $count -lt $howmany ]
do
echo "Image $count"
curl  http://lorempixel.com/400/400/food/ \
  -o "food_$count.jpg"
  sleep 30s
  count=`expr $count + 1`
done