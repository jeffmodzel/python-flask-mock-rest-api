from flask import Blueprint, jsonify, request
from werkzeug.exceptions import HTTPException
import database

bp = Blueprint('routes',__name__)
db = database.InMemoryDatabase()

@bp.route('/api/<resource>', methods=['GET','POST'])
@bp.route('/api/<resource>/<id>', methods=['GET','PUT','DELETE'])
def api_resource_route(resource,id=None):
    print(request)
    try:
        if request.method == 'GET':
            if id is None:
                database_response = db.get_all(resource)
                if database_response:
                    return jsonify(database_response)
                else:
                    return jsonify([])
            else:
                database_response = db.get_one(resource,id)
                if database_response:
                    return jsonify(database_response)
                else:
                    return jsonify({'message':'Resource {0} does not exist.'.format(id)}),404
        elif request.method == 'POST':
            data = request.get_json()
            database_response = db.add(resource,data)
            if database_response:
                return jsonify(database_response)
            else:
                return jsonify({'message':'Unable to process request.'}),400
        elif request.method == 'PUT':
            data = request.get_json()
            database_response = db.update(resource,id,data)
            if database_response:
                return jsonify(database_response)
            else:
                return jsonify({'message':'Resource {0} does not exist.'.format(id)}),404
        elif request.method == 'DELETE':
            database_response = db.remove(resource,id)
            if database_response:
                return jsonify(database_response)
            else:
                return jsonify({'message':'Resource {0} does not exist.'.format(id)}),404
        else:
            return jsonify({'message':'Unable to process request.'}),400

    except HTTPException as he:
        print(he)
        return jsonify({'message':he.description}),he.code
    except Exception as e:
        print(e)
        return 'Error',500
