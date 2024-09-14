
image_name:dot_product

setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
	
test:
	venv/bin/pytest src/test_main.py

lint:
	venv/bin/flake8 src/dotp.py

build:
	make setup
	make test
	make lint

runb:
	# make build
	python3 ./src/dotp.py "[1,2,3]" "[5,5,6]"

run:
	# make build
	python3 ./src/dotp.py "[1,2,3]" "[5,5,6]"
