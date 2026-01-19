FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    netcat-openbsd \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

COPY . /app

# Make wait-for-db.sh executable
RUN chmod +x /app/wait-for-db.sh

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
