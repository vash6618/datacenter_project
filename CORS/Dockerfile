FROM node:13.12.0-alpine

WORKDIR /cors
ENV PATH /cors/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

COPY . ./

EXPOSE 5005
CMD ["node", "cors-proxy.js"]