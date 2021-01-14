# docker build --target sa_web -t titedios/sa_web:0.1 .
# docker build --target sa_model -t titedios/sa_model:0.1 .

FROM python:3.6-alpine as builder

RUN apk update \
    && apk --no-cache --update add build-base cmake automake \
    gfortran openblas-dev lapack-dev cython \
    python3-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM builder as sa_web
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN ls .
EXPOSE 5000

FROM builder as sa_model
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "cervix/run_model_server.py" ]
