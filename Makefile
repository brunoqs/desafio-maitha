run:
	uvicorn app.main:app --reload

test:
	pytest

lint: 
	flake8 app
	isort --check-only app
	mypy .
	pylint --exit-zero app

format-code:
	black app
	isort app

before-commit: format-code lint test