import streamlit as st
import os

from pdf_loader import load_and_split
from rag import create_vector_db
from rag import ask_question


st.title("AI Document Assistant")

uploaded = st.file_uploader(
    "Upload PDF",
    type="pdf"
)


if uploaded:

    os.makedirs(
        "uploaded_docs",
        exist_ok=True
    )

    save_path = f"uploaded_docs/{uploaded.name}"

    with open(save_path, "wb") as f:

        f.write(uploaded.getbuffer())

    st.success("PDF uploaded")

    chunks = load_and_split(save_path)

    create_vector_db(chunks)

    st.success("Document processed")


query = st.text_input(
    "Ask a question"
)


if query:

    answer = ask_question(query)

    st.write(answer)