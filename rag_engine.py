from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_DIR = "vectorstore"

def get_answer(question: str):
    # 1️⃣ Load embeddings (same model as ingest.py)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 2️⃣ Load FAISS vector database
    db = FAISS.load_local(
        DB_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # 3️⃣ Retrieve relevant SOP chunks
    retriever = db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(question)

    if not docs:
        return "I don't know based on the provided SOPs.", []

    # 4️⃣ Build clean, readable answer (LINE BY LINE)
    answer_lines = []
    sources = set()

    for doc in docs:
        content = doc.page_content.strip()

        # Split SOP content into sentences
        sentences = content.split(". ")

        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and sentence not in answer_lines:
                answer_lines.append(sentence)

        sources.add(doc.metadata.get("source", "Unknown"))

        # STOP early to avoid dumping entire SOP
        if len(answer_lines) >= 5:
            break

    # 5️⃣ Format answer with proper new lines
    formatted_answer = ""
    for i, line in enumerate(answer_lines[:5], start=1):
        formatted_answer += f"{i}. {line}.\n"

    return formatted_answer.strip(), list(sources)
