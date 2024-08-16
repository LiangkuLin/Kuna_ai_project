# Law_Genius - Law & Chatgpt & Langchain Integration App
### Project initialization 

1. Set up running environment
    - Install [Anaconda](https://www.anaconda.com/download)
    - Open Anaconda and import the conda env file from this project 
    - (Optional) If conda env cannot be imported in Anaconda, please create a new python environment and install all dependencies manually 
    ```
    pip install python-dotenv langchain openai langchain-chroma langchain-openai flask waitress langchain-community langchain.chains pypdf
    ```

2. Create a .flaskenv file in the root folder of this project. 
    ```
    FLASK_APP=run.py
    FLASK_ENV=development
    OPENAI_API_KEY=xxxxx
    PINECONE_API_KEY=xxxx
    PINECONE_INDEX_NAME=xxxx
    REDIS_HOST=XXXX
    REDIS_PORT=1xxx
    REDIS_USERNAME=xxx
    REFIS_PASSWORD=xxxx
    ``` 
3. We are currently using a Pinecone database. Please open the terminal and cd to the manual folder. Run the following command to create the vector db (Note that dependencies are needed in this step)   
    ```
    python database.py
    ```

### Project Running
1. Open Anaconda and open the corresponding python environment terminal
2. CD to the project repository
3. Run project
    - Input this command (Note that the server will keep running, press Ctrl+C to terminate)
    ```
    waitress-serve --port=8080 run:app
    ```
### Docker 
1. To build image, run 
    ```
    docker build . -t [image name]:[tag]
    ```
2. To run container, run
    ```
    docker run --publish 8080:8080 --name [container name] [image name with tag]
    ```