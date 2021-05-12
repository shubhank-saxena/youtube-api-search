# pull official base image
FROM python:3.8.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# expose port
EXPOSE 8000

# install psycopg2 dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql libpq-dev \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock manage.py .env /usr/src/app/
RUN pipenv install --system --deploy --ignore-pipfile

COPY backend /usr/src/app/backend/
COPY docker /usr/src/app/docker

CMD [ "python", "manage.py", "collectstatic" ]
CMD ["chmod", "u+x", "/usr/src/app/docker/server/entrypoint.sh"]
ENTRYPOINT ["/usr/src/app/docker/server/entrypoint.sh"]