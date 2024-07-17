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
separator="\n",
    chunk_size = 2000,
    chunk_overlap = 200, 
)

loader = TextLoader("../data/data.txt",encoding='utf-8')
docs = loader.load_and_split(text_splitter)

print("開始Chroma綁定")
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory='../local_database'
)
print("完成Chroma綁定")
print("TestResult",db.similarity_search("民法第一條是什麼"))

