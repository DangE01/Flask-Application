install:
	pip install -r requirements.txt
run:
	python main.py
lint:
	pylint --disable=R,C main.py