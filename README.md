# Law_Genius - Law & Chatgpt & Langchain Integration App
### Project initialization 

### Project Running
1. Create a .flaskenv file in the root folder of this project
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

2. Set up running environment and run
    - Open termianl and head to WSL
    - CD to the project repository
    - Create running env 
    ```
    source virt/bin/activate
    ```
    - Run the following command to run this project 
    ```
    python application.py
    ```
### Deployment
1. Only several folders are needed when deployment
    ```
    app (folder)
    ebextensions (folder)
    .flaskenv (file)
    application.py (file)
    config.py (file)
    requirement.txt (file)
    ```
2. Zip these folders and upload to aws elastic beanstalk 

### Vector database 
1. We are currently using a Pinecone database. Please open the terminal and cd to the manual folder. Run the following command to create the vector db (Note that dependencies are needed in this step)   
    ```
    python database.py
    ```
