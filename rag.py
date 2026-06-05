from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

llm = Ollama(model="llama3")


def create_vector_db(chunks):

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("vector_store")


def load_db():

    return FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )


def ask_question(query):

    db = load_db()

    retriever = db.as_retriever(
        search_kwargs={"k":5}
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a document assistant.

Answer ONLY from the context.

If asked about projects, only list projects.

If asked about skills, only list skills.

If information is not present, say:
"I could not find this in the document."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response