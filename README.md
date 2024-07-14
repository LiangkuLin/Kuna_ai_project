# Ai_low Project - The langchain with Chatgpt testing project
### Project initialization 

1. Set up running environment
    - Install [Anaconda](https://www.anaconda.com/download) and create a new virtual environment
    - Open the virtual environment terminal and install all required packages
    ```
    pip install python-dotenv langchain openai langchain-chroma langchain-openai flask waitress langchain-community python-dotenv pypdf
    ```

2. Set up openai key in this project
   - create .env file in main folder and put the following key in it
    ```
    OPENAI_API_KEY=xxxx
    ```

4. Run project
    - In terminal, run 
    ```
    waitress-serve --port=8080 run:app
    ```
6. If the vector database is not created, please run the following command to create database
    - In terminal, run 
    ```
    python set_vector_database
    ```