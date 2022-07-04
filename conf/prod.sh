#!/usr/bin/env bash

IVETL_PROD=1
export IVETL_PROD

unset IVETL_LOCAL
unset IVETL_QA

IVETL_ROOT=/iv/impactvizor-pipeline
export IVETL_ROOT

IVETL_CASSANDRA_IP=10.0.1.93,10.0.1.116,10.0.1.248
export IVETL_CASSANDRA_IP

IVETL_TABLEAU_SERVER=reports-data.vizors.org
export IVETL_TABLEAU_SERVER

IVETL_TABLEAU_IP=10.0.1.44
export IVETL_TABLEAU_IP

IVETL_TABLEAU_HTTPS=1
export IVETL_TABLEAU_HTTPS


IVETL_TABLEAU_USERNAME=monitor
export IVETL_TABLEAU_USERNAME

IVETL_TABLEAU_PASSWORD=M5NbtYmT
export IVETL_TABLEAU_PASSWORD

IVETL_WEB_ADDRESS=https://manage.vizors.org
export IVETL_WEB_ADDRESS

DJANGO_SETTINGS_MODULE=ivweb.settings.prod
export DJANGO_SETTINGS_MODULE

IVETL_RABBITMQ_BROKER_URL="amqp://guest:guest@10.0.1.174:5672//;amqp://guest:guest@10.0.1.185:5672//"
export IVETL_RABBITMQ_BROKER_URL

IVETL_RATE_LIMITER_SERVER=10.0.1.174:8082
export IVETL_RATE_LIMITER_SERVER