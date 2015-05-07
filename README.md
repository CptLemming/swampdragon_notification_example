# Notification Example

## Install
```
pip install -r requirements.txt
python manage.py syncdb
```

## Run
```
// Webserver
python manage.py runserver 0.0.0.0:8000`

// Websocket server (2nd terminal)
python manage.py runsd
```

## Create notification
Browse to http://localhost:8000

Open a 2nd tab and browse to http://localhost:8000/admin/

Create a new notification and it should appear on the first browser window.
