# Flask-Boilerplate
This is the base of a web application in Flask to get you started and save time. The application run using gunicorn on a docker container thought a reverse proxy using NGINX and over HTTPS.

---

## Documentation and resources
[Docker multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/ "Docker multi-stage builds")<br />
[Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ "Best practices for writing Dockerfiles")
[Larger Applications](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/ "Larger Applications")<br />
[Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints "Modular Applications with Blueprints")<br />

## Tools I use for Web Application Development with Python and Flask
* [NGINX](https://www.nginx.com/ "NGINX")<br />
* [Docker](https://www.docker.com/ "Docker")<br />
* [Docker Compose](https://docs.docker.com/compose/ "Docker Compose")<br />
* [Bootstrap 4](https://getbootstrap.com/ "Bootstrap 4")<br />
* [Normalize CSS](https://necolas.github.io/normalize.css/ "Normalize CSS")<br />
* [Chart JS](https://www.chartjs.org/ "Chart JS")<br />
* [DataTables](https://www.datatables.net/ "DataTables")<br />
* [Font Awesome](https://fontawesome.com/ "Font Awesome")<br />
* [jQuery](https://jquery.com/ "jQuery")<br />
* [Modernizr](https://modernizr.com/ "Modernizr")<br />

## Python Libraries I use for Web Application Development with Python and Flask
* [Flask](https://flask.palletsprojects.com/en/1.1.x/ "Flask")<br />
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/ "Flask-Login")<br />
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/ "Flask-SQLAlchemy")<br />
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/ "Flask-Bcrypt")<br />
* [Flask-Security](https://pythonhosted.org/Flask-Security/ "Flask-Security")<br />
* [Flask-Uploads](https://pythonhosted.org/Flask-Uploads/ "Flask-Uploads")<br />
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/ "Flask-WTF")<br />
* [WTForms](https://wtforms.readthedocs.io/en/2.3.x/ "WTForms")<br />
* [email-validator](https://github.com/JoshData/python-email-validator "email-validator")<br />
* [gunicorn](https://gunicorn.org/ "gunicorn")<br />
* [pyOpenSSL](https://www.pyopenssl.org/en/stable/ "pyOpenSSL")<br />

---
![alt text][logo]

[logo]: https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png "Flask"

---

## For testing purposes
The application comes with test certs for testing only. Make sure you do not use them on production.
```ignorelang
/Flask-Boilerplate
    /services
        /reverse_proxy
            /certs
                cert.pem
                key.pem
```

The credentials to login and test are:<br />
Email: admin@example.local<br />
Password: Admin123<br />

## Directory structure
```ignorelang
/Flask-Boilerplate
    .gitattributes
    .gitignore
    docker-compose.yml
    LICENSE
    README.md
    /services
        /reverse_proxy
            Dockerfile
            webapp.conf
            /certs
        /web
            Dockerfile
            /web_app
                requirements.txt
                wsgi.py
                /myapp
                    __init__.py
                    forms.py
                    models.py
                    views.py
                    /blueprints
                    /static
                        /css
                        /js
                        /img
                        /vendors
                    /templates
```

---

# How to run the web application on any Operating System
```ignorelang
$ python3 wsgi.py
```

## How to run the web application with gunicorn (Mac and Linux)
NOTE: gunicorn does not work on Windows
In order to run the application run it with gunicorn using the following command:
```ignorelang
$ gunicorn -w 4 -b 0.0.0.0:5000 wsgi
```

---

## Layout.html
Page title
```ignorelang
{% block title %}
{% endblock title %}
```

CSS imports
```ignorelang
{% block css_import %}
{% endblock css_import %}
```

CSS Style - Already has the "style" tags added, no need to add them.
```ignorelang
{% block style %}
{% endblock style %}
```

Page content - The content block is right below page header inside the content area.
```ignorelang
{% block content %}
{% endblock content %}
```

JS Imports
```ignorelang
{% block js_import %}
{% endblock js_import %}
```

Script - Already has the "script" tags added, no need to add them.
```ignorelang
{% block script %}
{% endblock script %}
```

## How to build the docker image
Note: Run the following commands from the current directory where the Dockerfile is located.<br />

Lets build everything using docker-compose with the switch -d to run it on the background and --build to build everything.
```ignorelang
$ docker-compose up -d --build
```

To check the running containers
```ignorelang
$ docker-compose ps
```

If you want to bring down the web application and remove the images run.<br />
NOTE: This only removes the reverse proxy and web images
```ignorelang
$ docker-compose down --volume --rmi all
```

To remove all images that are not being used by a running container
```ignorelang
$ docker image prune -fa
```

To remove all volumes that are not being used by a running container
```ignorelang
$ docker volume prune -f
```

To remove all networks that are not being used by a running container
```ignorelang
$ docker network prune -f
```

To remove all containers that are not running
```ignorelang
$ docker container prune -f
```

## What if you need to export the images to another system?
Sometimes you need to development an internal application for a company and the production server has no access to the outside world so you have to build the images in your local computer, export them, and then load them on the server.<br />
Lets export our application images:
```ignorelang
$ docker save -o web_application.tar web_application:web_application
$ docker save -o reverse_proxy.tar reverse_proxy:reverse_proxy
```

To load the image on another server use the following command:
```ignorelang
$ docker load -i web_application.tar
$ docker load -i reverse_proxy.tar
```

Lets build a new docker-compose file and name it import-docker-compose.yml, Add the following code in the file.
```yaml
version: '3.7'
services:
  web_application:
    restart: always
    container_name: web_application
    image: web_application:web_application
    expose:
      - 5000
    entrypoint: ['gunicorn', '-w', '7', '-b', '0.0.0.0:5000', 'wsgi']
  reverse_proxy:
    restart: always
    container_name: reverse_proxy
    image: reverse_proxy:reverse_proxy
    depends_on:
      - web_application
    ports:
      - 443:443
      - 80:80
```

Lets build the containers using our new import-docker-compose file.
```ignorelang
$ docker-compose -f import-docker-compose.yml up -d
```

## What if you need to run your application over HTTPS while on development?
You can do so using ssl_context which create the certificates on the fly with the following code.
NOTE: to be able to use ssl_context you need to install the following
```ignorelang
$ pip install pyOpenSSL
```
```ignorelang
from flask import Flask

application = Flask(__name__)


@application.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    application.run(ssl_context='adhoc', host='0.0.0.0', port=443)

```

## Build the self-signed certificates
```ignorelang
$ openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```
