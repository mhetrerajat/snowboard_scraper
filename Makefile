.DEFAULT: help

help:
	@echo "make pretty - Does linting and deletes *.pyc files"

pretty:
	find . -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type f -name "*.py" -exec isort {} \;
	find . -type f -name "*.py" -exec python -m yapf --recursive --parallel --in-place --verbose --style=pep8 {} \;
