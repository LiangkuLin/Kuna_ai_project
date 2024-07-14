from langchain.document_loaders import UnstructuredXMLLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.document_loaders import PyPDFLoader


def createDatabase():
    embeddings = OpenAIEmbeddings()
    text_splitter = CharacterTextSplitter(
    separator="\f",
        chunk_size = 300,
        chunk_overlap = 100, 
    )
    loader = PyPDFLoader("data/data.pdf")
    print(loader)
    docs = loader.load_and_split(text_splitter)
    print(docs)

    db = Chroma.from_documents(
        docs,
        embedding=embeddings,
        # MySQL dirctory
        persist_directory='db'
    )
    print('Create vector database success')

    