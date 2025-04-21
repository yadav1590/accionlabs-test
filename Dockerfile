# used alpine image as base image
FROM nginx:1.19-alpine

# Remove the default nginx index page and placed small index page
RUN rm -rf /usr/share/nginx/html/*

# Copy your custom Nginx configuration (optional, if needed)
#COPY nginx.conf /etc/nginx/nginx.conf

# Copy your custom HTML content (optional)
COPY index.html /usr/share/nginx/html

# Expose only the required port
EXPOSE 80

# Start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
