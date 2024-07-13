from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
import argparse
import langchain
from langchain.prompts import PromptTemplate


langchain.debug = True

parser = argparse.ArgumentParser()
args = parser.parse_args()

load_dotenv()
embeddings = OpenAIEmbeddings()
chat =ChatOpenAI()

db = Chroma(
    persist_directory='判例db',
    # different from db creation
    embedding_function= embeddings,
)

prompt = PromptTemplate(template="請給我{task}此行為應依刑事訴訟法哪幾條?",input_variables=['task','heelo'])


retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(    
    llm = chat, 
    retriever = retriever,
    # "Stuffing" (injecting) into the system message 
    # Description 1: This is the default setting of chain_type. It just returns the "stuff that related to the user questions."
    # Description 2: If you set it to "map_reduce", the retreive algorithm will change. For more information, please go Udemy -> https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/learn/lecture/40261274?start=270#reviews 
    chain_type = "stuff",
)

# Question
result = chain.run("性侵會怎樣")
print(result)