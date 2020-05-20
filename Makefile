install:
	pip3 install -r requirements.txt
.PHONY: install

test:
	python -m pytest -v
.PHONY: test