from flask import Blueprint, jsonify,request
from app.model.response import ApiResponse
from app.util.length_check import checklength

api_langchain = Blueprint('langchain', __name__)

@api_langchain.route('/qs',methods=['POST'])
def question_database():
    data = request.get_json()
    # 檢查數據是否有缺漏
    if not data or 'question' not in data or 'session_id' not in data:
        return jsonify(ApiResponse("error","Invalid input. 'question' and 'session_id' are required").json), 400
    
    
    # 檢查數據是否為字串
    question = data.get('question')
    session_id = data.get('session_id')
    openai_key = data.get('openai_key')

    if not isinstance(question, str) or not isinstance(session_id, str) or not isinstance(openai_key, str):
        return jsonify(ApiResponse("error","question' and 'session_id' must be strings").json), 400
    
    
    # 於Langchain提問
    try:
        from app.service.prompt import queryQuestionFromDatabase 
        checklength(question,100)
        answer = queryQuestionFromDatabase(question,session_id,openai_key)
        
        #返回json
        return jsonify(ApiResponse(answer).json),200
    except Exception as error:
        return jsonify(ApiResponse("vector_database", error).json),500
    
    

   
   

