from flask import Blueprint, jsonify


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/message', methods=['GET'])
def get_example():
    return jsonify({'message': 'Welcome to your API using Blueprints.'})
