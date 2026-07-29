.PHONY: help run migrate createsuperuser test clean docker-up docker-down

help:
	@echo "Available commands:"
	@echo "  make help            - Show this help message"
	@echo "  make run             - Run the Django development server"
	@echo "  make migrate         - Apply database migrations"
	@echo "  make createsuperuser - Create a Django superuser"
	@echo "  make test            - Run Django tests"
	@echo "  make clean           - Remove Python cache and build artifacts"
	@echo "  make docker-up       - Start Docker containers"
	@echo "  make docker-down     - Stop Docker containers"

run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

test:
	python manage.py test

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -f db.sqlite3

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down