dev:
	@python3 manage.py runserver

migrations:
	@python3 manage.py makemigrations

migrate:
	@python3 manage.py migrate

test:
	@pytest -s -v

test_cov:
	@pytest -s -v --cov=.

test_overview:
	@python -m http.server 9000 --directory htmlcov

shell:
	@python manage.py shell_plus
