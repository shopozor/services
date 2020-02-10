FROM node:13.8.0-alpine

# TODO: copy consumer-ui code in some /data folder

RUN addgroup -S app && adduser -S -g app app

RUN apk --no-cache add ca-certificates

WORKDIR /root/

ENV NPM_CONFIG_LOGLEVEL warn

RUN mkdir -p /home/app

WORKDIR /home/app
COPY package.json ./

RUN yarn

COPY src src

# chmod for tmp is for a buildkit issue
RUN chown app:app -R /home/app \
    && chmod 777 /tmp

USER app

RUN touch /tmp/.lock

CMD ["yarn", "start"]