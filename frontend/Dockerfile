FROM node:9.6.1

RUN mkdir -p /opt/mattrosanio/frontend
COPY package.json /opt/mattrosanio/frontend
WORKDIR /opt/mattrosanio/frontend
RUN npm install

EXPOSE 3000