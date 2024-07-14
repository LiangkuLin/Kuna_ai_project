from flask import Blueprint, jsonify

from app.model.response import ApiResponse


api_test = Blueprint('test', __name__)

@api_test.route('/',methods=['GET'])
def test():
    return jsonify(ApiResponse("Test success").json),200


