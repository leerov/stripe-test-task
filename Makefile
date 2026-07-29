.PHONY: help setup-env install run migrate createsuperuser test clean up down docker-migrate docker-createsuperuser

help:
	@echo "Available commands:"
	@echo "  make help                 - Show this help message"
	@echo "  make setup-env            - Copy .env.example to .env if not exists"
	@echo "  make install              - Install Python dependencies locally"
	@echo "  make run                  - Run the Django development server locally"
	@echo "  make migrate              - Apply database migrations locally"
	@echo "  make createsuperuser      - Create a Django superuser locally"
	@echo "  make test                 - Run Django tests locally"
	@echo "  make clean                - Remove Python cache and build artifacts"
	@echo "  make up                   - Start Docker containers (and setup env)"
	@echo "  make down                 - Stop Docker containers"
	@echo "  make docker-migrate       - Apply database migrations in Docker"
	@echo "  make docker-createsuperuser - Create a Django superuser in Docker"
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

up: setup-env
	docker-compose up --build

down:
	docker-compose down
docker-migrate:
	docker-compose exec web python manage.py migrate

docker-createsuperuser:
	docker-compose exec web python manage.py createsuperuser
