install:
	python3 -m venv venv
	venv/bin/pip3 install --upgrade pip &&\
	venv/bin/pip3 install -r requirements.txt

format:	
	venv/bin/black src/*.py
	venv/bin/nbqa black src/*.ipynb

test:
	venv/bin/python3 -m pytest --nbval src/*.ipynb
	venv/bin/python3 -m pytest -vv --cov=src.lib

lint:
	venv/bin/nbqa ruff src/*.ipynb
	venv/bin/ruff check src/*.py

run:
	cat README.md.template > ./README.md
	venv/bin/python3 ./src/profile_report.py >> ./README.md
	chmod +x ./output_graph.png
	echo "![graph](./output_graph.png)" >> README.md


all: install lint run test format