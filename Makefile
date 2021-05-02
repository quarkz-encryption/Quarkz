.PHONY: install test

default: test

install:
    pip3 install --upgrade .

test:
    PYTHONPATH=. pytest
