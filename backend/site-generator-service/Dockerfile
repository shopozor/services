FROM node:13.8.0-alpine

# TODO: copy consumer-ui code in some /data folder
WORKDIR /data
# TODO: make sure I only need the consumer-ui folder for the sake of building
COPY ./frontend/consumer-ui/ .

# Site generator service app
RUN addgroup -S app && adduser -S -g app app
RUN apk --no-cache add ca-certificates
RUN mkdir -p /home/app
WORKDIR /home/app
COPY ./backend/site-generator-service/package.json ./package.json
COPY ./backend/site-generator-service/src src
RUN yarn
USER app
CMD ["yarn", "start"]
