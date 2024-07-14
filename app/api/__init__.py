from flask import Blueprint, jsonify

api_bp = Blueprint('apis', __name__)

@api_bp.route('/database/create',methods=['GET'])
def create_database():
    # try:
    #     print('work')
        from app.server.database import createDatabase
        createDatabase()
        return jsonify("DB create Success")
    # except:
    #       return jsonify("DB create fail")