from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

VERSION = os.environ.get('APP_VERSION','MISSING')
NAME = os.environ.get('APP_NAME','MISSING')
RUN_LOCAL = os.environ.get('RUN_LOCAL',None)
SERVER_START = datetime.now()

application = Flask(__name__)

import routes
application.register_blueprint(routes.bp)

@application.route('/',methods=['GET'])
def index():
    return render_template('index.html', health = get_health())

@application.route('/health',methods=['GET'])
def health():
    try:
        return jsonify(get_health())
    except Exception as e:
        print(e)
        return 'Error',500

def get_health():
    delta = datetime.now() - SERVER_START
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds,60*60)
    minutes, seconds = divmod(remainder,60)
    uptime = '{} hrs {} mins {} secs'.format(hours,minutes,seconds)
    database_status = routes.db.status()
    return {'name': NAME, 'version': VERSION, 'uptime': uptime, 'database': database_status, 'status': 'pass'}

if __name__ == "__main__":
    if RUN_LOCAL:
        application.debug = True
        application.run()
    else:
        application.run(host='0.0.0.0')
