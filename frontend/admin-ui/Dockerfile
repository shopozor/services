FROM node:13.8.0-alpine AS builder

WORKDIR /tmp
# we need to keep the folder structure like this, as we might have dependencies in shared stuff later on
COPY ./frontend/admin-ui/package.json ./frontend/admin-ui/package.json
COPY ./frontend/admin-ui/yarn.lock ./frontend/admin-ui/yarn.lock
WORKDIR /tmp/frontend/admin-ui
RUN yarn && yarn build
# TODO: build storybook too!

FROM nginx:1.16.0 AS app

COPY --from=builder /tmp/frontend/admin-ui/dist/spa /srv

# TODO: provide storybook image here!