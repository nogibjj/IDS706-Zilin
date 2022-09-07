install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv app/test_*.py

format:	
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py app/*.py 

all: install lint test