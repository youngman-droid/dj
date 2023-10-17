 
# syntax = docker/dockerfile:1

ARG NODE_VERSION=16.20.1
FROM node:${NODE_VERSION}-slim as base

# Node.js app lives here
WORKDIR /app

# Set production environment
ENV NODE_ENV="production"
ARG YARN_VERSION=1.22.10
RUN npm install -g yarn@$YARN_VERSION --force

# Throw-away build stage to reduce size of final image
FROM base as build

# Install packages needed to build node modules
RUN apt-get update -qq && \
    apt-get install -y build-essential pkg-config python

# Install node modules
COPY --link .npmrc package.json yarn.lock ./
RUN yarn install --frozen-lockfile --production=false

# Copy application code
COPY --link . .
#ENV REACT_APP_DJ_URL=
ENV REACT_USE_SSE=true
RUN yarn run build

# Remove development dependencies
RUN yarn install --production=true
# Final stage for app image
FROM pierrezemb/gostatic
# Copy built application
COPY --from=build /app/build/ /srv/http/DataJunction/dj/
