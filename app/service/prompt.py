import langchain
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from app.model.redis_db import RedisChatMessageHistory

import os



def queryQuestionFromDatabase(question:str, session_id:str , openai_key): 
        langchain.debug = True
        embeddings = OpenAIEmbeddings(
            api_key=openai_key
        )
        llm =ChatOpenAI(
            api_key=openai_key
        )
        db = PineconeVectorStore(embedding=embeddings,index_name=os.getenv("PINECONE_INDEX_NAME"))
        retriever =  db.as_retriever()
        ### Contextualize question ###
        contextualize_q_system_prompt = (
            "Given a chat history and the latest user question "
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        history_aware_retriever = create_history_aware_retriever(
            llm, retriever, contextualize_q_prompt
        )

        ### Answer question ###
        system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Answer should be in traditional chinese in default."
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use ten sentences maximum and keep the "
            "answer concise." 
            "{context}"
        )
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
       
        ### Statefully manage chat history ###
        
  
        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )
    
        result= conversational_rag_chain.invoke(
            {"input": question},
            config={
                "configurable": {"session_id": session_id}
            },
        )["answer"]
        return result
        

# Stringfy docs for prompt 
def format_docs(docs: list[Document]):
    stringDoc = ""
    for doc in docs:
        stringDoc = stringDoc+doc.page_content+ "\n"
    return stringDoc

# 604800 ->　1 week 
def get_session_history(session_id: str) -> RedisChatMessageHistory:
    return  RedisChatMessageHistory(session_id,"message_store:",604800 )
