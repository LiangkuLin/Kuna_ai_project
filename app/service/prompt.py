import langchain
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate

def queryQuestionFromDatabase(question): 
    try:
        langchain.debug = True
        embeddings = OpenAIEmbeddings()
        chat =ChatOpenAI()

        # Read db here 
        db = Chroma(
            persist_directory='db',
            # different from db creation
            embedding_function= embeddings,
        )

        retriever = db.as_retriever()
        
        # propmpt
        prompt = ChatPromptTemplate(
        input_variables=["context"],
        messages=[
            SystemMessagePromptTemplate.from_template("You are a Taiwan law expert, able to answer relative law questions as hard as possible"),
            HumanMessagePromptTemplate.from_template("{context}")
        ]
)

        chain = RetrievalQA.from_chain_type(    
            llm = chat, 
            retriever = retriever,
            chain_type = "stuff",
            chain_type_kwargs = {"prompt": prompt}    
        )

        # Question
        result = chain({"query": question})
        return result
    except Exception as error: 
         raise  Exception(error)