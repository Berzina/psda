web: gunicorn smarthome.wsgi --log-file -
python manage.py collectstatic --noinput
sock: python websocket_server.py