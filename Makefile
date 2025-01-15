PYTHON=python
PIP=pip
MANAGE=manage.py

install:
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) $(MANAGE) migrate

runserver:
	$(PYTHON) $(MANAGE) runserver

createsuperuser:
	$(PYTHON) $(MANAGE) createsuperuser

collectstatic:
	$(PYTHON) $(MANAGE) collectstatic --noinput

test:
	$(PYTHON) $(MANAGE) test

freeze:
	$(PIP) freeze > requirements.txt

shell:
	$(PYTHON) $(MANAGE) shell

lint:
	flake8 .

format:
	black .

.PHONY: install migrate runserver createsuperuser collectstatic test freeze shell lint format