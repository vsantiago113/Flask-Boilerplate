FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY webapp.conf /etc/nginx/conf.d/webapp.conf
COPY certs /certs
RUN apk update && apk add bash