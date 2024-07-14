# import langchain
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

def queryQuestionFromDatabase(question): 
    try:
        # langchain.debug = True
        embeddings = OpenAIEmbeddings()
        chat =ChatOpenAI()

        # Read db here 
        db = Chroma(
            persist_directory='db',
            # different from db creation
            embedding_function= embeddings,
        )

        retriever = db.as_retriever()

        chain = RetrievalQA.from_chain_type(    
            llm = chat, 
            retriever = retriever,
            chain_type = "stuff",
        )

        # Question
        result = chain.run(question)
        return result 
    except Exception as error: 
         raise  Exception(error)