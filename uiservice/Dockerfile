FROM node:13.12.0-alpine

WORKDIR /foofi
ENV PATH /foofi/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts -g --silent

COPY . ./
RUN chmod 777 ./docker.sh

CMD ["./docker.sh"]