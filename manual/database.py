from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredXMLLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader

load_dotenv(dotenv_path='../.flaskenv')

embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(
separator="\f",
    chunk_size = 1000,
    chunk_overlap = 100, 
)
loader = TextLoader("../data/data.txt")
docs = loader.load_and_split(text_splitter)
print(docs)
db = Chroma.from_documents(
    docs,
    embeddings,
    # MySQL dirctory
    persist_directory='../local_database'
)
query = "民法第一條是啥"
result = db.similarity_search(query)
print("Test Result: ",result) 