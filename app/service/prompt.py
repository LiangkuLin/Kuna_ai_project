import langchain
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate, SystemMessagePromptTemplate,AIMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableSerializable
from langchain_core.documents import Document
from langchain.memory import ConversationBufferMemory
from langchain import hub

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
                SystemMessagePromptTemplate.from_template("Please respond to the question according to your previous answer. If you cannot find the answer in that, please respond to the question using the provided documents. The documents are {context}. All answer should be in Chinese. If the answer cannot be found in the documents, please indicate that you are don't know the answer."),
                # Can put all previous reqesuts and answers here 
                HumanMessagePromptTemplate.from_template("How long are you?"),
                AIMessagePromptTemplate.from_template("I am 30 cm"),
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
        # Can stroe the messages here 

        return result


# Stringfy docs for prompt 
def format_docs(docs: list[Document]):
    stringDoc = ""
    for doc in docs:
        stringDoc = stringDoc+doc.page_content+ "\n"
    return stringDoc