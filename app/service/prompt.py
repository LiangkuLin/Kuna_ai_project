import langchain
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate

def queryQuestionFromDatabase(question): 
        langchain.debug = True
        embeddings = OpenAIEmbeddings()
        chat =ChatOpenAI()
        # Read db here 
        db = Chroma(
            # different from db creation
            embedding_function= embeddings,
            persist_directory='local_database',
        )
        retriever = db.as_retriever()
        chain = RetrievalQA.from_chain_type(    
            llm = chat, 
            retriever = retriever,
            chain_type = "stuff",
        )

        # Question
        result = chain(question)
        print("++++++++++++++++++++++++++++++++++++++++++++++++", result)
        return result
