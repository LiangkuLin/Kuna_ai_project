from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores.chroma import Chroma


load_dotenv(dotenv_path='../.flaskenv')

embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(
separator="\f",
    chunk_size = 1000,
    chunk_overlap = 100, 
)
loader = PyPDFLoader("../data/data.pdf")
docs = loader.load_and_split(text_splitter)
print(docs)
db = Chroma.from_documents(
    docs,
    embeddings,
    # MySQL dirctory
    persist_directory='../local_database'
)
print('Database create success')