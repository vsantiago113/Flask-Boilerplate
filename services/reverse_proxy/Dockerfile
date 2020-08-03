# NGINX Docker Official Images: https://hub.docker.com/_/nginx/
FROM nginx:alpine

# Update the system and install bash to be able to execute commands.
RUN apk update && apk add --no-cache bash

# Remove the default.conf file and copy our webapp.conf file.
RUN rm /etc/nginx/conf.d/default.conf
COPY webapp.conf /etc/nginx/conf.d/webapp.conf

# Copy our certs to /certs directory.
COPY certs /certs

## Add permissions for nginx user.
#RUN chown -R nginx:nginx /certs && chmod -R 755 /certs && \
#        chown -R nginx:nginx /var/cache/nginx && \
#        chown -R nginx:nginx /var/log/nginx && \
#        chown -R nginx:nginx /etc/nginx/conf.d
#RUN touch /var/run/nginx.pid && \
#  chown -R nginx:nginx /var/run/nginx.pid && \
#  chown -R nginx:nginx /var/cache/nginx
#
## Switching to a non-root user.
#USER nginx
