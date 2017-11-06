install:
	pip install -r requirements.txt

runserver:
	python manage.py runserver

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

test:
	python manage.py test