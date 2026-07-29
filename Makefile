.PHONY: help run migrate createsuperuser test clean docker-up docker-down setup-env

help:
	@echo "Available commands:"
	@echo "  make help            - Show this help message"
	@echo "  make setup-env       - Copy .env.example to .env if not exists"
	@echo "  make run             - Run the Django development server"
	@echo "  make migrate         - Apply database migrations"
	@echo "  make createsuperuser - Create a Django superuser"
	@echo "  make test            - Run Django tests"
	@echo "  make clean           - Remove Python cache and build artifacts"
	@echo "  make docker-up       - Start Docker containers"
	@echo "  make docker-down     - Stop Docker containers"

setup-env:
	@if [ ! -f .env ]; then cp .env.example .env; echo ".env created from .env.example"; else echo ".env already exists"; fi

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