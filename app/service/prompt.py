import langchain
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableSerializable
from langchain_core.documents import Document


# from app.model.retriever import RedundantFilterRetriever
import os 

def queryQuestionFromDatabase(question): 
        langchain.debug = True
        embeddings = OpenAIEmbeddings()
        llm =ChatOpenAI()
        # Read db here 
        db = PineconeVectorStore(embedding=embeddings,index_name=os.getenv("PINECONE_INDEX_NAME"))
      
        prompt = ChatPromptTemplate(
            input_variables=["question","context"],
            messages=[
                SystemMessagePromptTemplate.from_template("Please respond to the question using the provided documents and in Traditional Chinese. The documents are {context}. If the answer cannot be found in the documents, please indicate that you are humor."),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )
        
    
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