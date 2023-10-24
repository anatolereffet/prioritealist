install:
	poetry install

lint:
	poetry run black prioritealist tests
	poetry run mypy prioritealist
	poetry run pylint --rcfile .pylintrc prioritealist tests

test:
	poetry run pytest -v --cov=prioritealist/

safety :
	poetry run safety check

docs: docs/source/*
	poetry run sphinx-build -b html docs/source docs/build