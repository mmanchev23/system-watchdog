FROM node:18.17.0-alpine

WORKDIR /client

COPY . /client/

RUN yarn

EXPOSE 5173:5173

CMD [ "yarn", "run", "dev", "--host" ]
