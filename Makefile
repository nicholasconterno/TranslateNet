.PHONY: lint run test

lint:
    flake8 .

run:
    python app.py

test:
    pytest
