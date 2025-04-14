from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

pdf_path = "E:\project\Mayank Pandey_Resume.pdf"
persist_directory = "E:\\project\\database"
loader = PyPDFLoader(pdf_path)
pages = loader.load()
# print(pages)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.split_documents(pages)
# print(docs)

embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
vectordb = Chroma.from_documents(documents=docs, embedding=embedding_model, persist_directory=persist_directory)

print("✅ PDF data embedded and stored!")
count = vectordb._collection.count()
print(f"✅ Total embeddings stored: {count}")


