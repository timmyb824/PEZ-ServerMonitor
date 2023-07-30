run-app:
	@echo "Running app via local config"
	python src/main.py -a

run-pre-commit:
	@echo "Running pre-commit"
	pre-commit run --all-files

run-coverage-tests:
	@echo "Running coverage tests"
	coverage run -m pytest -xv tests/

run-coverage-report:
	@echo "Running coverage report"
	coverage report -m