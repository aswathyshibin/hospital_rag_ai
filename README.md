<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/2966/2966487.png" alt="Hospital AI" width="120" style="border-radius:12px;"/>

<h1>Hospital SOP AI Assistant</h1>

<h3>AI-Powered Retrieval Augmented Generation (RAG) System</h3>

<h4>Developed by <b>Aswathy Shibin</b></h4>

<p>
An intelligent hospital policy assistant that answers doctors’ and nurses’ questions  
<b>strictly from uploaded SOP documents</b> using modern AI.
</p>

</div>

---

## 🔍 Overview

The **Hospital SOP AI Assistant** is a **real-world healthcare AI project** built using  
**LLMs + Retrieval Augmented Generation (RAG)** architecture.

Instead of training a model from scratch, this system:
- Indexes hospital SOP documents (PDF/TXT)
- Stores them as vector embeddings
- Retrieves only relevant policy sections
- Generates accurate, grounded answers  

⚠️ **No hallucination. No external guessing. Only SOP-based answers.**

---

## 🎯 Project Objectives

- 📘 Provide instant access to hospital SOPs  
- 🧑‍⚕️ Help doctors & nurses clarify protocols quickly  
- 🔐 Ensure policy-safe and controlled AI responses  
- ⚡ Enable real-time document updates without retraining  
- 🌐 Deploy as a professional web application (Render-ready)

---

## 🚀 Key Features

### 📄 SOP Upload (PDF & TXT)
- Upload new SOP files anytime
- Automatically indexed into vector database
- No model retraining required

### 🤖 RAG-Based Question Answering
- Uses semantic search + LLM
- Answers strictly from hospital documents
- Responds *“I don’t know based on SOPs”* if not found

### 🔍 Source Transparency
- Displays SOP file names used for each answer
- Ensures auditability and trust

### 🎨 Professional Web Interface
- Clean hospital-style UI
- Background image & modern buttons
- Responsive and user-friendly

---

## 🧠 RAG Architecture (Concept)

<div align="center">

User Question
↓
Vector Search (FAISS)
↓
Relevant SOP Chunks
↓
LLM Answer Generation
↓
Verified Hospital Policy Answer

</div>

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| **Backend** | Python, Flask |
| **RAG Framework** | LangChain |
| **Embeddings** | Sentence Transformers (MiniLM) |
| **Vector DB** | FAISS |
| **LLM** | Hugging Face / OpenAI (configurable) |
| **Frontend** | HTML, CSS |
| **Deployment** | Render |

---

## 📂 Project Structure

hospital_rag_ai/
│
├── app.py # Flask application
├── rag_engine.py # RAG logic
├── ingest.py # SOP indexing pipeline
├── requirements.txt
│
├── data/ # Uploaded SOP files
├── vectorstore/ # FAISS index
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── README.md


---

## 🔄 Workflow

1️⃣ Upload SOP document  
2️⃣ Document chunking & embedding  
3️⃣ Stored in FAISS vector database  
4️⃣ User asks a question  
5️⃣ Relevant SOP chunks retrieved  
6️⃣ AI generates policy-accurate answer  

---

## 🌐 Deployment (Render)

- Push project to GitHub
- Create **Web Service** in Render
- Set:
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `python app.py`
- Add environment variables if using OpenAI
- Done 🚀

---

## ⚠️ Disclaimer

> This system is for **hospital SOP reference only**.  
> It does **not** provide medical advice or clinical decisions.

---

## 👩‍💻 Author

**Aswathy Shibin**  
AI | Data Science | Healthcare AI  
📍 India  

---

<div align="center">

⭐ *If you like this project, give it a star on GitHub!* ⭐

</div>
