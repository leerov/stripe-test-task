setup-env:
	@if [ ! -f .env ]; then cp .env.example .env; echo ".env created from .env.example"; else echo ".env already exists"; fi

install:
	python3 -m pip install -r requirements.txt

run:
	python3 manage.py runserver 0.0.0.0:8000

migrate:
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser

test:
	python3 manage.py test

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -f db.sqlite3

docker-up: setup-env
	docker-compose up --build

docker-down:
	docker-compose down