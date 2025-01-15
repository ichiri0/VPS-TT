PYTHON=python
PIP=pip
MANAGE=manage.py

install:
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) $(MANAGE) migrate

generate:
	$(PYTHON) $(MANAGE) makemigrations

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

docker:
	docker-compose up --build -d

docker-test:
	docker-compose up --build
	
.PHONY: install migrate runserver createsuperuser collectstatic test freeze shell lint format