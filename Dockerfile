FROM python:3.12-slim

WORKDIR /app

# Install MySQL client + netcat (needed by wait-for-db.sh)
RUN apt-get update && \
    apt-get install -y default-mysql-client netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . /app

# Make wait-for-db.sh executable
RUN chmod +x /app/wait-for-db.sh

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (fallback)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
