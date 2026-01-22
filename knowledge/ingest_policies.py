from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


# Load PDF
loader = PyPDFLoader(r"C:\Users\LENOVO\Downloads\company policy doc.pdf")
docs = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in vector DB
vectorstore = Chroma.from_documents(chunks, embeddings)
