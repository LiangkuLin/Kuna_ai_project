from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredXMLLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import PyPDFLoader
import time
import numpy as np
import os 

load_dotenv(dotenv_path='../.flaskenv')

embeddings = OpenAIEmbeddings(show_progress_bar=True)
text_splitter = CharacterTextSplitter(
separator="\n",
    chunk_size = 2000,
    chunk_overlap = 500, 
)

 # First Data 
loader = TextLoader("../data/data.txt", encoding = 'utf-8')
docs = loader.load_and_split(text_splitter)

print("開始Pinecone綁定")
db = PineconeVectorStore(embedding=embeddings,index_name=os.getenv("PINECONE_INDEX_NAME"))
split_Docs = np.array_split(docs, 20)
try:
    for doc in split_Docs:
        db.add_documents(doc)
        print("完成階段embed")
        print("開始休息")
        time.sleep(75)
        print("休息完成，繼續運作")
except Exception as error: 
        raise  Exception(error)
print("Pinecone綁定成功")
