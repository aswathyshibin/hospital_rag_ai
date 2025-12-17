from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_DIR = "vectorstore"

def get_answer(question: str):
    # Load embeddings (same model used in ingest.py)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS DB
    db = FAISS.load_local(
        DB_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Retrieve top SOP chunks
    retriever = db.as_retriever(search_kwargs={"k": 2})
    docs = retriever.invoke(question)

    if not docs:
        return "I don't know based on the provided SOPs.", []

    # Build a clean professional answer
    answer_lines = []
    sources = set()

    for doc in docs:
        text = doc.page_content.strip()
        if text and text not in answer_lines:
            answer_lines.append(text)
        sources.add(doc.metadata.get("source", "Unknown"))

    # LIMIT answer size (important!)
    answer = " ".join(answer_lines)
    answer = answer[:700]  # prevents SOP dumping

    return answer, list(sources)
