from app import create_app
from dotenv import load_dotenv
from pathlib import Path 

load_dotenv(dotenv_path='./.flaskenv')
app = create_app()

if __name__ == "__main__":
    app.run(port=8080)