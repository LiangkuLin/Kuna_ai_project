import langchain
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate
# from app.model.retriever import RedundantFilterRetriever
import os 

def queryQuestionFromDatabase(question): 
        langchain.debug = True
        embeddings = OpenAIEmbeddings()
        chat =ChatOpenAI()
        # Read db here 
        db = PineconeVectorStore(embedding=embeddings,index_name=os.getenv("PINECONE_INDEX_NAME"))
      
        retriever= db.as_retriever()
        chain = RetrievalQA.from_chain_type(    
            llm = chat, 
            retriever = retriever,
            chain_type = 'stuff',
        )
    

        # Question
        result = chain(question)
        return result
