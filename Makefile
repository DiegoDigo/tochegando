install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

runserver:
	python manage.py runserver

test:
	python manage.py test