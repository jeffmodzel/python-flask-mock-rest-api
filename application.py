from flask import Flask, request, jsonify
from datetime import datetime
import os

VERSION = os.environ.get('APP_VERSION','MISSING')
NAME = os.environ.get('APP_NAME','MISSING')
RUN_LOCAL = os.environ.get('RUN_LOCAL',None)
SERVER_START = datetime.now()

application = Flask(__name__)

import routes
application.register_blueprint(routes.bp)

@application.route('/')
def hello_world():
    print('hit the base url')
    return 'Mock Rest API' + VERSION

@application.route('/health',methods=['GET'])
def health():
    try:
        delta = datetime.now() - SERVER_START
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds,60*60)
        minutes, seconds = divmod(remainder,60)
        uptime = '{} hrs {} mins {} secs'.format(hours,minutes,seconds)
        data = {'name' : NAME,'version' : VERSION,'uptime' : uptime,'database' : routes.db.status()}
        return jsonify(data)
    except Exception as e:
        print(e)
        return 'Error',500

if __name__ == "__main__":
    if RUN_LOCAL:
        application.debug = True
        application.run()
    else:
        application.run(host='0.0.0.0')
