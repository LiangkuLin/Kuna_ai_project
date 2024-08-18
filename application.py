from app import create_app
from dotenv import load_dotenv
from pathlib import Path 

load_dotenv(dotenv_path='./.flaskenv')
application = create_app()

if __name__ == "__main__":
    application.run(port=8080)