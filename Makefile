install:
	poetry install

lint:
	poetry run black .
	poetry run mypy .
	poetry run pylint prioritealist tests

test:
	poetry run pytest -v --cov=prioritealist/


docs:
	poetry run sphinx-build -b html docs/source docs/build