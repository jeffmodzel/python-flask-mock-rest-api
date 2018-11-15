# python-flask-mock-rest-api
Mock Rest API implemented in python (with flask) and deployable to AWS Elastic Beanstalk.

If you're looking for a simple Flask / Elastic Beanstalk example check out [eb-python-flask](https://github.com/aws-samples/eb-python-flask).

# the code & readme doc is still in progress - 11/15/18

## Overview

## Install

only two dependencies - flask and pytest

run locally like ...

## Details

no auth
use local object db

## AWS Stuff

Getting AWS setup and configured is outside the scope of this document, however it is not terribly difficult.

High level steps
1 Have AWS account, have keys configured
2 Make a basic Python Beanstalk app
2 Get AWS CLI installed
3 run scripts

Links to AWS doc here
https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/index.html

confusing parts of elastic beanstalk - application, environment, etc
url is available in console

## build and deploy helper scripts

build assumes you have zip installed in your command line environment. link to zip

deployment takes a couple minutes
deployment is driven by the app version in the shell script
