# Extra pytest arguments, e.g. `make test PYTEST_ARGS=tests/test_greet.py`.
PYTEST_ARGS ?=

.PHONY: test
test:
	python -m pytest $(PYTEST_ARGS)
