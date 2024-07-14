# Ai_low Project - The langchain with Chatgpt testing project
### Project initialization 

1. Set up running environment
    - Install [Anaconda](https://www.anaconda.com/download) and create a new virtual environment
    - Open the virtual environment terminal and install all required packages
    ```
    pip install python-dotenv langchain openai langchain-chroma langchain-openai flask waitress langchain-community langchain.chains python-dotenv pypdf
    ```

2. Create .flaskenv file in this project
    ```
    FLASK_APP=run.py
    FLASK_ENV=development
    OPENAI_API_KEY=xxxxx
    ```

### Project Running
1. Run Anaconda and open the corresponding terminal
2. CD to the project repository
3. Run project
    - In terminal, input this command
    ```
    waitress-serve --port=8080 run:app
    ```