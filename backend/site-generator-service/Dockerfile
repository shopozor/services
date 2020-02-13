FROM node:13.8.0-alpine

RUN apk --no-cache add ca-certificates

RUN mkdir -p /data/frontend/consumer-ui
COPY ./frontend/consumer-ui/package.json /data/frontend/consumer-ui
COPY ./frontend/consumer-ui/yarn.lock /data/frontend/consumer-ui
WORKDIR /data/frontend/consumer-ui
RUN yarn

COPY ./backend/site-generator-service/package.json /app/package.json
COPY ./backend/site-generator-service/yarn.lock /app/yarn.lock
WORKDIR /app
RUN yarn

COPY ./frontend/consumer-ui/ /data/frontend/consumer-ui
COPY ./shared/graphql /data/shared/graphql
COPY ./backend/site-generator-service/src /app/src
COPY ./backend/site-generator-service/entrypoint.sh /app/entrypoint.sh

RUN chmod u+x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
