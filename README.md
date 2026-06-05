# AI Document Assistant (RAG-Based)

# Overview

AI Document Assistant is a Retrieval Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them using natural language queries. Instead of manually searching through lengthy documents, users can ask questions and receive context-aware answers generated from the document's content.

The application processes uploaded PDFs, converts document text into vector embeddings, stores them in a FAISS vector database, retrieves the most relevant information through semantic search, and generates accurate responses using Llama 3 running locally via Ollama.

# Features

* Upload and process PDF documents
* Natural language question answering
* Semantic search using vector embeddings
* Context aware response generation
* Local LLM inference with Llama 3
* Interactive Streamlit based user interface
* Fast retrieval using FAISS vector database

# How It Works

1. User uploads a PDF document.
2. Text is extracted using PyPDFLoader.
3. Document content is split into smaller chunks using LangChain.
4. Sentence Transformer embeddings are generated for each chunk.
5. Embeddings are stored in a FAISS vector database.
6. User submits a question.
7. The query is converted into an embedding vector.
8. FAISS retrieves the most relevant document chunks.
9. Retrieved context is passed to Llama 3 through Ollama.
10. The model generates a context aware answer based on the document content.

# Tech Stack

1. Frontend

* Streamlit

2. Backend

* Python
* LangChain

3. Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

4. Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

5. Vector Database

* FAISS

6. Large Language Model

* Llama 3
* Ollama

# Project Architecture

PDF Upload
- Text Extraction
- Text Chunking
- Embedding Generation
- FAISS Vector Storage
- Similarity Retrieval
- Context Construction
- Llama 3 Generation
- Final Response

# Key Learning Outcomes

* Retrieval Augmented Generation (RAG)
* Vector Embeddings and Semantic Search
* FAISS Vector Databases
* LangChain Framework
* Prompt Engineering
* Local LLM Deployment with Ollama
* Building AI Applications with Streamlit

# Future Improvements

* Multi document support
* Source citations and page references
* Conversational memory
* Document summarization
* Cloud deployment
* User authentication and document management

# Author
Haryash Singh

Built as a practical implementation of Retrieval Augmented Generation (RAG) to explore document intelligence, semantic search, and Large Language Model integration.

