# Personal Website
Scott Angelius

## Stack
- Python 3.10
- Django 4.1
- MySQL 8.0

## Install
In website directory:
python -3.10 -m venv .venv
git clone repo

Create database:
mysql -u root -p -e "CREATE DATABASE scottangelius CHARACTER SET utf8; CREATE USER '[username]'@'localhost' IDENTIFIED BY '[password]'; GRANT ALL PRIVILEGES ON scottangelius.* TO '[username]'@'localhost'; FLUSH PRIVILEGES;"

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
