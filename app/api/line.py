from flask import Blueprint, jsonify,request
from app.model.response import ApiResponse
from app.util.length_check import checklength
import json

from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
import os 
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from app.service.prompt import queryQuestionFromDatabase


line = Blueprint('line', __name__)

@line.route("", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_TOKEN'))
    handler = WebhookHandler(os.getenv('LINE_SECRETE'))
    signature = request.headers['X-Line-Signature']
    handler.handle(body, signature)
    tk = json_data['events'][0]['replyToken']
    msg = json_data['events'][0]['message']['text']
    userId =getUserId(json_data['events'])
    reply_msg = ''
    reply_msg = queryQuestionFromDatabase(msg,userId)
    text_message = TextSendMessage(text=reply_msg)
    line_bot_api.reply_message(tk,text_message)
    return ""
    
def getUserId(events): 
    for event in events:
        if event['type'] == 'message':
            user_id = event['source']['userId']
            return user_id