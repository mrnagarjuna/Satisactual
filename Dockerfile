FROM python:3.12-slim

WORKDIR /app

# Install MySQL client
RUN apt-get update && apt-get install -y \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

# Make script executable INSIDE the image
RUN chmod +x /app/wait-for-db.sh

RUN pip install --no-cache-dir -r requirements.txt

