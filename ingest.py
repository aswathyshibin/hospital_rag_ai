import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_DIR = "data"
DB_DIR = "vectorstore"

def ingest_documents():
    documents = []

    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)

        if file.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()

        elif file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            docs = loader.load()

        else:
            continue

        for d in docs:
            d.metadata["source"] = file

        documents.extend(docs)

    if not documents:
        print("⚠️ No documents found")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if os.path.exists(DB_DIR):
        db = FAISS.load_local(DB_DIR, embeddings, allow_dangerous_deserialization=True)
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, embeddings)

    db.save_local(DB_DIR)
    print("✅ SOP documents indexed successfully")

if __name__ == "__main__":
    ingest_documents()
