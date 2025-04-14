==============================
🧠 AI Resume Query Web App
==============================

This is a Flask-based web application that allows users to query information from an embedded PDF resume using a Large Language Model (LLM) and vector store.

------------------------------------
📁 Project Structure
------------------------------------
- ingest.py              → Script to load PDF, split text, embed using HuggingFace, and store in ChromaDB
- q_a.py                 → Main Flask app to handle LLM querying and web routing
- templates/index.html   → HTML form for user query input
- database/              → Chroma vector store directory
- Mayank Pandey_Resume.pdf → PDF file to be queried
- .env                   → Environment file to store HuggingFace API key
- requirements.txt       → All required Python dependencies

------------------------------------
🧠 Features
------------------------------------
✔️ Query any resume-style PDF using natural language  
✔️ Uses HuggingFace Zephyr LLM for smart responses  
✔️ Stores data in Chroma vector database for fast retrieval  
✔️ Simple HTML frontend  
✔️ Loader message ("Please wait...") after submit  
✔️ Clean footer "Powered by Mayank"

------------------------------------
⚙️ How to Run
------------------------------------

1️⃣ Install all dependencies:

```bash
pip install -r requirements.txt

python q_a.py
