install:
	poetry install

lint:
	poetry run black prioritealist tests
	poetry run mypy prioritealist
	poetry run pylint prioritealist tests

test:
	poetry run pytest -v --cov=prioritealist/


docs: docs/source/*
	poetry run sphinx-build -b html docs/source docs/build