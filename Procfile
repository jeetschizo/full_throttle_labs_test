web: gunicorn full_throttle_labs.wsgi --workers 5 --timeout 120 --keep-alive 5 --log-level debug
release: python manage.py migrate