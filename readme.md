# Trainee

Trainee Management System

## Installation

```bash
pip install requirements.txt
```

## Connect to Mysql Then Run Those Command

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Using Docker
```
sudo docker-compose up 
```
## Migration
```
sudo docker exec traineemanagement_web_1 python manage.py migrate 
```
