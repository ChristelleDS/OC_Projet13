FROM python:3.10.2-slim-buster

# copier fichiers vers nouveau repertoire
ADD . /appDocker
# changer le répertoire de travail
WORKDIR /appDocker

# installer les requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
VOLUME /appDocker/logs

# collect static files
#  RUN python manage.py collectstatic --noinput

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
