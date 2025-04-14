# from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from flask import Flask, request, render_template
# import streamlit as st
load_dotenv()
app = Flask(__name__)
 
persist_directory = r"E:\project\database"
def qa_retr():
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    print(vectordb._collection.count())

    llm = HuggingFaceEndpoint(repo_id = "HuggingFaceH4/zephyr-7b-beta", task = "text-generation")
    model = ChatHuggingFace(llm = llm)
    # query = "What is the contact number?"

    qa_chain = RetrievalQA.from_chain_type(
            llm=model,
            retriever=vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
            chain_type="stuff"
        )
    return qa_chain

def ask_query(query):
    pre = qa_retr()
    # if pre != None:
    result = pre.invoke({"query": query})
    return result['result']



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def greet():
    name = request.form["name"]  
    result = ask_query(name)
    # print(result)
    return f"<h2>{result}</h2>"     




if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


