from flask import Blueprint, jsonify,request
from app.model.response import ApiResponse

api_langchain = Blueprint('langchain', __name__)

@api_langchain.route('/qs',methods=['GET'])
def question_database():
    from app.service.prompt import queryQuestionFromDatabase 
    try:
        question = request.args.get('question')
        answer = queryQuestionFromDatabase(question)
        return jsonify(ApiResponse(answer).json),200
    except Exception as error:
        return jsonify(ApiResponse("Vector取資失敗", error).json),500

@api_langchain.route('/create',methods=['POST'])
def create_database():
    try:
        from app.service.database import createDatabase
        print('Vector建立中')
        createDatabase()
        print('Vector建立完成')
        return jsonify(ApiResponse('Vector建立完成').json),200
    except Exception as error:
        return jsonify(ApiResponse("Vector建立失敗", error).json),500