web: gunicorn smarthome.wsgi --log-file -
python manage.py collectstatic --noinput
python websocket_server.py