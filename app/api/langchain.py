from flask import Blueprint, jsonify,request
from app.model.response import ApiResponse
from app.util.length_check import checklength
from app.service.classification import classifiedQuestion


api_langchain = Blueprint('langchain', __name__)

@api_langchain.route('/qs',methods=['GET'])
def question_database():
    question = request.args.get('question')
    session_id= request.args.get('session_id')
    if not question or not session_id:
        return jsonify(ApiResponse("query_params", "missing query data").json), 400
    
    try:
        from app.service.prompt import queryQuestionFromDatabase 
        question = request.args.get('question')
        session_id= request.args.get('session_id')
        checklength(question,100)
        
        # data proccess
        # answer = queryQuestionFromDatabase(question,session_id)
        answer = classifiedQuestion(question)
        return jsonify(ApiResponse(answer).json),200
    except Exception as error:
        return jsonify(ApiResponse("question_error", error).json),500
