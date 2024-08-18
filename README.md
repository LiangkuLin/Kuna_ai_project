# Law_Genius - Law & Chatgpt & Langchain Integration App
### Project Initialization
1. Open a terminal and switch to WSL
2. Navigate to the project directory
3. Create a virtual environment named 'virt':
    ```
    virtualenv virt
    ```
4. Activate the virtual environment:
    ```
    source virt/bin/activate
    ```
5. Install all the required dependencies (from requitements.txt):
    ```
    pip install -r requirements.txt
    ```

### Running the Project
1. Create a .flaskenv file in the root directory of the project with the following content:
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

2. To run the project:
    - Open a terminal and switch to WSL
    - Navigate to the project directory
    - Activate the virtual environment:
    ```
    source virt/bin/activate
    ```
    - Start the project:
    ```
    python application.py
    ```
### Deployment (optional)
1. The following folders and files are needed for deployment:
    ```
    app (folder)
    ebextensions (folder)
    .flaskenv (file)
    application.py (file)
    config.py (file)
    requirement.txt (file)
    ```
2. Zip these folders and upload them to AWS Elastic Beanstalk

### Update requirement.txt (optional)
    - To list all dependencies in the virtual environment: 
    ```
    pip freeze
    ```
    - To update the requirements.txt file with the current dependencies
    ```
    pip freeze > requirements.txt
    ```

### Vector database (optional)
1. We are using a Pinecone database. To create the vector database, navigate to the manual folder and run the following command (ensure all dependencies are installed):
    ```
    python database.py
    ```
