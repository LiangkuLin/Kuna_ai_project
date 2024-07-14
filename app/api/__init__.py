from flask import Blueprint, jsonify

api_bp = Blueprint('apis', __name__)

@api_bp.route('/database/create',methods=['POST'])
def create_database():
    try:
        from app.server.database import createDatabase
        print('Vector建立中')
        createDatabase()
        print('Vector建立完成')
        return jsonify({"message":'Vector建立完成'}),200 
    except Exception as error:
          return jsonify({"message":"Vector建立失敗"}),500