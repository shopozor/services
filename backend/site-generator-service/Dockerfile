FROM node:13.8.0-alpine

# consumer-ui code
RUN mkdir -p /data/frontend/consumer-ui
COPY ./frontend/consumer-ui/package.json /data/frontend/consumer-ui
COPY ./frontend/consumer-ui/yarn.lock /data/frontend/consumer-ui
WORKDIR /data/frontend/consumer-ui
RUN yarn
COPY ./frontend/consumer-ui/ ./frontend/consumer-ui
COPY ./shared/graphql ./shared/graphql

# site generator service app
RUN apk --no-cache add ca-certificates
COPY ./backend/site-generator-service/package.json /app/package.json
COPY ./backend/site-generator-service/yarn.lock /app/yarn.lock
WORKDIR /app
RUN yarn
COPY ./backend/site-generator-service/src src
CMD ["yarn", "start"]
