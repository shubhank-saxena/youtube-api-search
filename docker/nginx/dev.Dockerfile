FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY docker/nginx/nginx-proxy.conf /etc/nginx/conf.d
EXPOSE 80