# Python Docker Official Images: https://hub.docker.com/_/python/
FROM python:3.8.5-slim-buster

# Expose port 5000 internally only to other containers in the same network.
EXPOSE 5000

# Keeps Python from generating .pyc files in the container.
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging.
ENV PYTHONUNBUFFERED 1

# For Debuggable tracebacks on crashes in C code.
ENV PYTHONFAULTHANDLER=1

# Copy the web application content to /web_app directory and set it as the working directory.
WORKDIR /web_app
COPY web_app /web_app

# Install pip requirements.
RUN pip install --no-cache-dir --quiet -r requirements.txt

# Compile installed code:
RUN python -c "import compileall; compileall.compile_path(maxlevels=10)"

# Compile code in a directory:
RUN python -m compileall .


# Switching to a non-root user.
RUN useradd --create-home appuser && chown -R appuser /web_app
USER appuser

# Run the web application with Gunicorn
CMD gunicorn -w 7 -b 0.0.0.0:5000 wsgi
