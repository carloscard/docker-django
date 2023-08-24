FROM python:3.9
RUN apt-get -y update

# Install cron.
RUN apt-get install -y cron && touch /var/log/cron.log
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "iati_project", "iati_project.wsgi:application"]