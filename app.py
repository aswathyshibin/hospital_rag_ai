from flask import Flask, render_template, request
import os
from ingest import ingest_documents
from rag_engine import get_answer

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    sources = []

    if request.method == "POST":
        action = request.form.get("action")

        # 🔹 SOP FILE UPLOAD
        if action == "upload":
            file = request.files.get("sop_file")

            if file and file.filename:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)

                # Re-ingest documents
                ingest_documents()

                answer = "✅ SOP uploaded and indexed successfully."
                sources = [file.filename]

        # 🔹 QUESTION ASK
        elif action == "ask":
            question = request.form.get("question")
            if question:
                answer, sources = get_answer(question)

    return render_template("index.html", answer=answer, sources=sources)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)