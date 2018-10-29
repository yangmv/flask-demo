From python:3.6-alpine

ADD . /data1/www
WORKDIR /data1/www
RUN pip install flask
CMD ['python', 'app.py']