from flask import Flask, request
import os

application = Flask(__name__)
app_version = os.environ.get('APP_VERSION')

@application.route('/')
def hello_world():
    print('hit the base url')
    return 'Hello, World!'

@application.route('/api/<resource>')
def show_user_profile(resource):
    print(request)
    return 'Resource %s' % resource

@application.route('/health')
def health():
    return 'Health check' + app_version

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #app.debug = True
    application.run(host='0.0.0.0')
