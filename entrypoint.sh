#!/bin/sh

echo "Waiting for MySQL..."

python << END
import time
import MySQLdb

while True:
    try:
        MySQLdb.connect(
            host="db",
            user="ram",
            passwd="its",
            db="satisactual_1",
            port=3306
        )
        print("MySQL is ready!")
        break
    except Exception as e:
        print("MySQL not ready, waiting...")
        time.sleep(2)
END

python manage.py makemigrations
python manage.py migrate --noinput

exec python manage.py runserver 0.0.0.0:8000