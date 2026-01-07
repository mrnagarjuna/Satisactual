# Use Python 3.12 slim
FROM python:3.12-slim

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    gcc \
    python3-dev \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

# Default command: wait for DB, migrate, then run server
CMD ["sh", "-c", "./wait-for-db.sh db python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
