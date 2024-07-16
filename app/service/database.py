from langchain_community.document_loaders import UnstructuredXMLLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings

def createDatabase():
    try:
        embeddings = OpenAIEmbeddings()
        text_splitter = CharacterTextSplitter(
        separator="\n",
            chunk_size = 1000,
            chunk_overlap = 100, 
        )
        loader = TextLoader("data/data.txt", encoding = 'UTF-8')
        docs = loader.load_and_split(text_splitter)
        db = Chroma.from_documents(
            docs,
            embeddings,
            persist_directory='local_database'
        )
        return db 
    except Exception as error: 
         raise  Exception(error)

    