install:
	pip install -r requirements.txt

test:
    python manage.py migrate
	python manage.py test
