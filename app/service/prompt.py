import langchain
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain import hub

# from app.model.retriever import RedundantFilterRetriever
import os 

def queryQuestionFromDatabase(question): 
        langchain.debug = True
        embeddings = OpenAIEmbeddings()
        llm =ChatOpenAI()
        # Read db here 
        db = PineconeVectorStore(embedding=embeddings,index_name=os.getenv("PINECONE_INDEX_NAME"))
 
        prompt = hub.pull("rlm/rag-prompt")
    
        chain = (
            {
                "context": db.as_retriever() | format_docs,
                "question": RunnablePassthrough(),
            }
            | prompt
            | llm
            | StrOutputParser()
        )
     
        
        # Question
        result = chain.invoke(question)
        return result


# Stringfy docs for prompt 
def format_docs(docs: list[Document]):
    stringDoc = ""
    for doc in docs:
        stringDoc = stringDoc+doc.page_content+ "\n"
    return stringDoc