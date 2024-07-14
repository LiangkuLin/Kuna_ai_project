from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def makeQuestion(db_name,question): 
    
    # langchain.debug = True
    embeddings = OpenAIEmbeddings()
    chat =ChatOpenAI()

    db = Chroma(
        persist_directory=db_name,
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
    print(result)