# *code & readme is still in progress - 11/16/18*

# python-flask-mock-rest-api
Mock Rest API implemented in Python (with Flask) and deployable to AWS Elastic Beanstalk.

If you're looking for a simple Flask / Elastic Beanstalk example check out [eb-python-flask](https://github.com/aws-samples/eb-python-flask).

## Overview

Exposes a REST endpoint in the form of **api/{resource}** that accepts GET/POST/PUT/DEL and allows dynamic creation of resources. The REST endpoints available are:

* GET api/{resource}
* GET api/{resource}/{id}
* POST api/{resource}
* PUT api/{resource}/{id}
* DEL api/{resource}/{id}
* GET /health

For example if you wanted to create a person resource, you would call:
```
 POST api/person
 {"first_name": "Darth", "last_name": "Vader"}

 Returns 200
 {"first_name": "Darth", "last_name": "Vader", "id" : "9a02bcdc-439f-4726-9d80-8e15979ead18"}
```
When a resource is created (on POST) it is automatically assigned a UUID id. That id is then used to retrieve the resource like:
```
 GET api/person/9a02bcdc-439f-4726-9d80-8e15979ead18

 Returns 200
 {"first_name": "Darth", "last_name": "Vader", "id" : "9a02bcdc-439f-4726-9d80-8e15979ead18"}
```
Or remove the resource like:
```
 DEL api/person/9a02bcdc-439f-4726-9d80-8e15979ead18

 Returns 200
 {"first_name": "Darth", "last_name": "Vader", "id" : "9a02bcdc-439f-4726-9d80-8e15979ead18"}
```
All operations GET/POST/PUT/DEL on a resource echo back the resource in the response, not just GETs.

## Use Case
The motivation behind this project was mocking the behavior of an ERP system REST API. When writing software that integrates different software systems, it can be difficult if not impossible to have those software systems available during all phases of software development.  Especially when those different systems are large ERPs. This project is one way to mitigate that issue by creating a generic REST API that can serve as a mock for a large software system.

For example, let's say we're writing software that has to integrate with a large Human Resource system that exposes a REST API. During local development it may not be practical to have your own copy of that Human Resource system. Instead we would use a mock REST API to provide the functionality we expect. The HR system might have an API that exposes these types of resources:

* Employees
* Performance Reviews
* Timesheets
* Paychecks

And the REST API might look something like:

* http://hr-server/api/employees
* http://hr-server/api/performance-reviews
* http://hr-server/api/timesheets
* http://hr-server/api/paychecks

We could run this project and load up our mock server with resources by POSTing employees/performance-reviews/timesheets/paychecks. More....


## Install
The initial development was done in Python 3.5 and there are only two dependencies. Pytest is not really required unless you want to run the tests.

```
pip3 install Flask
pip3 install pytest
```

To run locally, execute the *run_local.sh* script:
```
export RUN_LOCAL=True
export APP_VERSION=1.0.0
export APP_NAME=python-flask-mock-rest-api
python3 application.p
```
Which just sets up some environment variables the code is looking for. To run the unit tests simply run:
```
pytest
```
There are different ways to structure a Flask project and many guides on best practices. This project was setup to be as easy as possible to deploy to Elastic Beanstalk.

More info on Flask and Pytest can be found:
links here

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

add postman subscriptions
update /root UI
add logger?


no business logic, can create multiple people with same name (they get different ids)
possibly add a query param thing for searching
