# Law_Genius - Law & Chatgpt & Langchain Integration App

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

2. Set up python environment and run project
    - Open termianl and head to WSL
    - CD to the project repository
    - Create running env 
    ```
    source virt/bin/activate
    ```
    - Run this project 
    ```
    python application.py
    ```
### Deployment (optional)
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

### Update requirement.txt (optional)
    - Check all dependencies in venv (virt)
    ```
    pip freeze
    ```
    - Update dependencies in requirement.txt
    ```
    pip freeze > requirements.txt
    ```

### Vector database (optional)
1. We are currently using a Pinecone database. Please open the terminal and cd to the manual folder. Run the following command to create the vector db (Note that dependencies are needed in this step)   
    ```
    python database.py
    ```
