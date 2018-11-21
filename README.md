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

Included in this project is a Postman collection and environment with example usage. Postman is an API Development and Testing tool - https://www.getpostman.com/

## Use Case
The motivation behind this project was mocking the behavior of an ERP system REST API. When writing software that integrates different software systems, it can be difficult if not impossible to have those software systems available during all phases of software development.  Especially when those different systems are large ERPs. This project is one way to mitigate that issue by creating a generic REST API that can serve as a mock for a large software system.

For example, let's say we're writing software that has to integrate with a large Human Resource System that exposes a REST API. During local development it may not be practical to have your own copy of that Human Resource System. Instead we would use a mock REST API to provide the functionality we expect. The Human Resource System might have an API that exposes these types of resources:

* Employees
* Performance Reviews
* Timesheets
* Paychecks

And the REST API might look something like:

* http://hr-server/api/employees
* http://hr-server/api/performance-reviews
* http://hr-server/api/timesheets
* http://hr-server/api/paychecks

We could run this project (locally or hosted somewhere like AWS) and load up our mock server with data by POST-ing employees, performance-reviews, timesheets and paychecks resources. Then we could work on our software and run against:

* http://local-server/api/employees
* http://local-server/api/performance-reviews
* http://local-server/api/timesheets
* http://local-server/api/paychecks

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

## Details
The web server in this project is relatively simple and is meant as a starting point for a more complicated or detailed use case. There is no authorization for requests or query string parameters for filtering or querying data. If these are required for your particular use case you would need to implement them.

The "database" used in this project is a simple, object data store implemented in-memory (i.e., not persistent). It is designed to store resources by type and takes the liberty of assigning unique UUID's to all new resources. There is no further business logic implemented - you can POST the same resource over and over and they will be created successfully each with a new UUID. If you need more complicated logic or persistent storage you would need to implement that.

## AWS Elastic Beanstalk
A secondary goal of this project was to create something that could easily be deployed to AWS. Getting AWS setup and configured is outside the scope of this document, however it is not terribly difficult. The high level steps are:

* Get an AWS account
* [Install the AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/).
* [Set up AWS Credentials for AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
* [Create the Elastic Beanstalk application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)

The easiest way to get started is to create the initial Elastic Beanstalk application manually in the AWS console. Create a new application for the Python platform and select Sample application. This will help you verify everything is setup correctly. You can then use the deploy script to replace the sample application code. The terminology can get a little confusing but the basic concept is that there are is an Elastic Beanstalk *application* and an *environment*.  An *environment* is a combination of *version* and *configuration*. The deploy script creates a new *version* and updates the *environment* to use the new *version*. You can read all about it here [What is AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html).

## build and deploy helper scripts

note - used AWS CLI not the EB CLI
Links to AWS doc here
https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/index.html

build assumes you have zip installed in your command line environment. link to zip

deployment takes a couple minutes
deployment is driven by the app version in the shell script

where is the url?
url is available in console

add postman subscriptions
update /root UI
add logger?


no business logic, can create multiple people with same name (they get different ids)
possibly add a query param thing for searching
