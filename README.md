# Ai_low Project - The langchain with Chatgpt testing project
### Project initialization 

1. Set up running environment
    - Install [Anaconda](https://www.anaconda.com/download)
    - Open Anaconda and import the conda env file from this project 
    - (Optional) If conda env cannot be imported in Anaconda, please create a new python environment and install all dependencies manually 
    ```
    pip install python-dotenv langchain openai langchain-chroma langchain-openai flask waitress langchain-community langchain.chains python-dotenv pypdf
    ```

2. Create .flaskenv file in the root folder of this project
    ```
    FLASK_APP=run.py
    FLASK_ENV=development
    OPENAI_API_KEY=xxxxx
    ```
3. (Optional) If the local_database not exist, use terminal and cd to the manual folder and run the following command to create the vector db. Note that dependencies are needed in this step. 
    ```
    python database.py
    ```

### Project Running
1. Open Anaconda and open the corresponding python environment terminal
2. CD to the project repository
3. Run project
    - In terminal, input this command (Note that the server will keep running, press ctrl+c to terminate)
    ```
    waitress-serve --port=8080 run:app
    ```