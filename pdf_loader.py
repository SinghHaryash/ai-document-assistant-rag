from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re


def clean_text(text):

    # Fix spaced letters:
    text = re.sub(
        r'(?<=\b[A-Z])\s(?=[A-Z]\b)',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text


def load_and_split(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    for doc in docs:

        doc.page_content = clean_text(
            doc.page_content
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        docs
    )

    return chunks