FROM alpine:latest
WORKDIR /run/nginx
RUN apk add --no-cache nginx
RUN chown -R nginx:nginx /var/lib/nginx
COPY static/default.conf /etc/nginx/http.d
COPY static/index.html /var/lib/nginx/html
EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
