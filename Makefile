setup:
	pip install -r requirements.txt
run:
	export FLASK_APP=flaskr/__init__.py
	export FLASK_ENV=development
	flask run


