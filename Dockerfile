FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
		gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev libffi-dev libressl-dev cargo openssl-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN mkdir /mediafiles
RUN adduser -D user
RUN chown -R user:user /code
RUN chown -R user:user /mediafiles
RUN chmod -R 755 /code
RUN chmod -R 755 /mediafiles