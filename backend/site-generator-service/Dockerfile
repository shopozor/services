FROM node:13.8.0-alpine

# consumer-ui code
WORKDIR /data
COPY ./frontend/consumer-ui/ ./frontend/consumer-ui
COPY ./shared/graphql ./shared/graphql
RUN cd ./frontend/consumer-ui && yarn

# site generator service app
RUN apk --no-cache add ca-certificates
RUN mkdir -p /app
WORKDIR /app
COPY ./backend/site-generator-service/package.json ./package.json
COPY ./backend/site-generator-service/src src
RUN yarn
CMD ["yarn", "start"]
