# pulling official node image
FROM node:12.16.1-alpine

# set workdir
WORKDIR /usr/src/app

# export port
EXPOSE 3000

# copy package.json & yarn.lock
COPY package.json .
COPY yarn.lock .
COPY craco.config.js .

# install dependencies
RUN yarn

# copy other files/directories
COPY public /usr/src/app/public
COPY src /usr/src/app/src/
COPY .env .

# build react static file
RUN yarn build
RUN yarn global add serve

CMD ["serve", "-p", "3000", "-s", "build"]