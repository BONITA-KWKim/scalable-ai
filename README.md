# A scalable deep learning rest API

This repository contains the code for scalable deep learning REST API.

## Prerequisites

Dependencies or configurations are written already. You just get this repo.

`
$ git clone https://github.com/BONITA-KWKim/***

I assume you already have __anaconda__ and __docker__(with __docker compose__) installed 
on your system. From there you need to create your virtual environment(venv).

`
$ conda env create -f **.yaml
`

## Getting started

Some packages are needed to install your venv. However, if venv was created, 
installation would be finished.

Command below is working to manually install those.

`
$ pip install flask gevent requests
`

## Starting the server

`
$ docker-compose up --build
`

## Submitting request to the Server

Requests can be submitted via cURL:
`
$ curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
`

