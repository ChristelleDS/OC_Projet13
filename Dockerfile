FROM python:3.10.2-slim-buster

# créer répertoire
RUN mkdir -p /appDocker
# copier fichiers vers nouveau repertoire
COPY . /appDocker
# changer le répertoire de travail
WORKDIR /appDocker

# installer python et les requirements
RUN apt-get update && apt-get install -y python3 python3-pip
&& pip install --upgrade pip \
&& pip install -r requirements.txt

EXPOSE 8000
VOLUME /appDocker/logs

# CMD python manage.py runserver
CMD gunicorn oc_lettings_site.wsgi
