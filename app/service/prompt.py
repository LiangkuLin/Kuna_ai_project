import langchain
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.prompts import PromptTemplate

def queryQuestionFromDatabase(question): 
        langchain.debug = True
        embeddings = OpenAIEmbeddings()
        chat =ChatOpenAI()

        # Read db here 
        db = Chroma(
            # different from db creation
            embedding_function= embeddings,
            persist_directory='../../local_database',
        )

        retriever = db.as_retriever()
        
        # propmpt
        prompt =PromptTemplate(
            input_variables=["context_str", "question"],
            template="With context of {context_str}. Please answer the following question. {question}. If the context is not provided, just answer the question.", 
        )

        chain = RetrievalQA.from_chain_type(    
            llm = chat, 
            retriever = retriever,
            chain_type = "stuff",
            chain_type_kwargs ={"prompt":prompt,"document_variable_name": "context_str"}
        )

        # Question
        result = chain.run(question)
        return result
