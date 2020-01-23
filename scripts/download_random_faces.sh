#!/bin/sh

# try http://lorempixel.com/400/400/food/ too
# try https://picsum.photos/ for shop pics

if [ ! -z "$1" ] && [ "$1" -eq "$1" ]; then
  howmany=`expr $1 + 1`
else
  howmany="10"
fi

count=1
while [ $count -lt $howmany ]
do
echo "Image $count"
curl 'https://thispersondoesnotexist.com/image'                                        \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'\
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'         \
  -H 'Accept-Language: en-US,en;q=0.8,fr-FR;q=0.5,fr;q=0.3' --compressed               \
  -H 'Connection: keep-alive'                                                          \
  -H 'Upgrade-Insecure-Requests: 1'                                                    \
  -H 'If-Modified-Since: Thu, 28 Mar 2019 12:31:58 GMT'                                \
  -H 'If-None-Match: W/"5c9cbebe-c2285"'                                               \
  -H 'Cache-Control: max-age=0'                                                        \
  -H 'TE: Trailers'                                                                    \
  -o "face_$count.jpg"
  sleep 2s
  count=`expr $count + 1`
done