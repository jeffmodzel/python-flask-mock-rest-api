
from flask import Blueprint, jsonify, request
from werkzeug.exceptions import HTTPException

bp = Blueprint('routes',__name__)

#from .. import database
#db = database.InMemoryDatabase()

#VERSION = '1.0.0'
#SERVER_START = datetime.now()

@bp.route('/test')
def hello2():
    return 'test'
