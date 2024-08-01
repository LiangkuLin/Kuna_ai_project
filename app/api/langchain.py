from flask import Blueprint, jsonify,request
from app.model.response import ApiResponse

api_langchain = Blueprint('langchain', __name__)

@api_langchain.route('/qs',methods=['GET'])
def question_database():
    from app.service.prompt import queryQuestionFromDatabase 
    try:
        question = request.args.get('question')
        session_id= request.args.get('session_id')
        answer = queryQuestionFromDatabase(question,session_id)
        return jsonify(ApiResponse(answer).json),200
    except Exception as error:
        return jsonify(ApiResponse("Vector取資失敗", error).json),500
