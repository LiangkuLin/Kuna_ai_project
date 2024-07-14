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

4. Run project
    - In terminal, run 
    ```
    waitress-serve --port=8080 run:app
    ```
6. If the vector database is not created, please run the following command to create database
    - In terminal, run (deprecated, just use postman to call api for now)
    ```
    python set_vector_database
    ```