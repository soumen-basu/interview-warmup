# ==========================================
# Stage 1: Build Static HTML via Quartz
# ==========================================
FROM node:22-slim AS builder

WORKDIR /app/quartz

# Install git required for plugin installation
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY quartz/package.json quartz/package-lock.json* ./
RUN npm ci

# Copy quartz engine files
COPY quartz/ ./

# Copy site configuration from root repository
COPY quartz.config.yaml ./quartz.config.yaml

# Copy wiki content
COPY wiki/ /app/wiki/

# Build static bundle
RUN npm run quartz -- build -d /app/wiki -o /app/public

# ==========================================
# Stage 2: Serve via Nginx (Production Parity)
# ==========================================
FROM nginx:alpine AS preview

# Copy custom Nginx configuration
COPY <<'EOF' /etc/nginx/conf.d/default.conf
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    # Compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript image/svg+xml;

    location / {
        try_files $uri $uri.html $uri/ /index.html =404;
    }

    # Static caching
    location ~* \.(?:ico|css|js|gif|jpe?g|png|webp|woff2?|eot|ttf|svg)$ {
        expires 6M;
        access_log off;
        add_header Cache-Control "public, max-age=15552000, immutable";
    }

    error_page 404 /404.html;
}
EOF

# Copy built static files from builder
COPY --from=builder /app/public /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
