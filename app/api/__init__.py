from flask import Blueprint, jsonify,request

api_bp = Blueprint('api', __name__)

@api_bp.route('/database/qs',methods=['GET'])
def question_database():
    from app.server.prompt import queryQuestionFromDatabase 
    try:
        question = request.args.get('question')
        answer = queryQuestionFromDatabase(question)
        return jsonify({"message":answer}),200
    except Exception as error:
        return jsonify({"message":"Vector取資失敗"}),500

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