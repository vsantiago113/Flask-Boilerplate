# Flask-Boilerplate
This is the base of a web application in Flask to get you started and save time. I decided to go with the following directory structure from the Flask documentation because it makes sense to me when running the web application on a Docker container and I just have to pass Docker a "command flask run" to start the web application.

---

## Documentation and resources
[Flask Official Documentation](https://flask.palletsprojects.com/en/1.1.x/ "Flask Official Documentation")<br />
[Larger Applications](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/ "Larger Applications")<br />
[Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints "Modular Applications with Blueprints")<br />

I am using the following Bootstrap Template "SB Admin 2" from Start Bootstrap<br />
[Start Bootstrap](https://startbootstrap.com/themes/sb-admin-2/ "SB Admin 2")

---
![alt text][logo]

[logo]: https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png "Flask"

---

## Directory structure
```ignorelang
/Flask-Boilerplate
    setup.py
    /application
        __init__.py
        views.py
        /blueprints
            example
        /static
            style.css
        /templates
            layout.html
            index.html
            login.html
            ...
```

---

## How to run the web application
In order to run the application you need to export an environment variable that tells Flask where to find the application instance:
```ignorelang
$ export FLASK_APP=application
```

If you are outside of the project directory make sure to provide the exact path to your application directory. Similarly you can turn on the development features like this:
```ignorelang
$ export FLASK_ENV=development
```

Assign the host ip for your application
```ignorelang
$ export FLASK_RUN_HOST=0.0.0.0
```

Assign the port your application will be listening for incoming connections
```ignorelang
$ export FLASK_RUN_PORT=8000
```

In order to install and run the application you need to issue the following commands:
```ignorelang
$ pip install -e .
$ flask run
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

The sidebar title on the upper left corner
```ignorelang
{% block side_bar_title %}
{% endblock side_bar_title %}
```

Profile name
```ignorelang
{% block profile_name %}
{% endblock profile_name %}
```

Profile image - the block is already inside the src attribute right inside the double quotes already. Just add the image path or image url.
```ignorelang
{% block profile_img %}
{% endblock profile_img %}
```

Page header
```ignorelang
{% block page_header %}
{% endblock page_header %}
```

Page sub header
```ignorelang
{% block page_sub_header %}
{% endblock page_sub_header %}
```

Page contentb - The content block is right below page header inside the content area.
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

Lets build everything using docker-compose with the switch -d to run it on the background.
```ignorelang
$ sudo docker-compose up -d
```

If you want to stop the web application run.
```ignorelang
$ sudo docker-compose down
```

If you don't have docker-compose then build the image manually.
```ignorelang
$ sudo docker build . --tag "flask-boilerplate:flask-boilerplate"
```

Lets build the container using docker run.
```ignorelang
$ sudo docker run -d -p 5000:5000 --name web_app flask-boilerplate:flask-boilerplate
```

If you need to export the image after creating it use the following command
```ignorelang
$ sudo docker save -o /docker_images/flask-boilerplate.tar flask-boilerplate:flask-boilerplate
```

To load the image on another server use the following command
```ignorelang
$ sudo docker load -i /docker_images/flask-boilerplate.tar
```
