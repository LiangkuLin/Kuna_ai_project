from langchain.document_loaders import UnstructuredXMLLoader
from langchain.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.document_loaders import PyPDFLoader

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
   separator="\f",
    chunk_size = 1000,
    chunk_overlap = 0, 
)
loader = PyPDFLoader("./data/最高法院刑事庭具有參考價值之裁判要旨暨裁判全文（113年4月）.pdf")
print(loader)
docs = loader.load_and_split(text_splitter)
print(docs)

db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    # MySQL dirctory
    persist_directory='判例db'
)