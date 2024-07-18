from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredXMLLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain_community.vectorstores.chroma  import Chroma
from langchain_community.document_loaders import PyPDFLoader
import time
import numpy as np

load_dotenv(dotenv_path='../.flaskenv')

embeddings = OpenAIEmbeddings(show_progress_bar=True)
text_splitter = CharacterTextSplitter(
separator="\n",
    chunk_size = 1000,
    chunk_overlap = 100, 
)

 # First Data 
loader = TextLoader("../data/data.txt", encoding = 'utf-8')
docs = loader.load_and_split(text_splitter)

print("開始Chroma綁定")
split_Docs = np.array_split(docs, 12)
db = Chroma(embedding_function=embeddings,persist_directory='../local_database')
# db.add_documents(docs)
try:
    for doc in split_Docs:
        db.add_documents(doc)
        print("完成階段embed")
        print("開始休息")
        time.sleep(75)
        print("休息完成，繼續運作")
except Exception:
    print("Error",Exception)

print("Chroma綁定成功")
