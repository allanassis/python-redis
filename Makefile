setup:
	pip install -r requirements.txt
run:
	gunicorn flaskr:create_app


