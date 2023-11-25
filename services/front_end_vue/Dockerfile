FROM node:16-alpine

WORKDIR /app
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

ENV PATH /app/node_modules/.bin:$PATH

RUN yarn global add @vue/cli

COPY package.json .
COPY package-lock.json .
RUN yarn
