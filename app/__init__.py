from flask import Flask
from config import BASE_API_ROUTE
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config')
     
     # Register blueprints
    from app.api import api_test
    from app.api.langchain import api_langchain
    app.register_blueprint(api_test, url_prefix=f'/{BASE_API_ROUTE}')
    app.register_blueprint(api_langchain, url_prefix=f'/{BASE_API_ROUTE}/database')
    # init line 
    from app.api.line import line
    app.register_blueprint(line,url_prefix=f'/{BASE_API_ROUTE}/line')
    return app 