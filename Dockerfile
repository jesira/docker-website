FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
RUN python manage.py collectstatic --noinput
RUN mkdir /code/media
RUN chmod -R 755 /code/media
CMD [ "python","manage.py","runserver","0.0.0.0:8000"  ]