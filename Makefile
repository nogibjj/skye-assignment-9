install:
	python3 -m venv venv
	venv/bin/pip3 install --upgrade pip &&\
	venv/bin/pip3 install -r requirements.txt

format:	
	venv/bin/black src/*.py
	venv/bin/nbqa black src/*.ipynb

test:
	venv/bin/python3 -m pytest --nbval src/*.ipynb

lint:
	venv/bin/nbqa ruff src/*.ipynb
	venv/bin/ruff check src/*.py


all: install lint test format