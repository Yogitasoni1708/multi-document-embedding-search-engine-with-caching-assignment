# Multi-Document Embedding Search Engine with Caching  
AI Engineer Intern Assignment – CodeAtRandom AI

# 📌 Overview

''' This repository implements a semantic search engine over 100–200 documents, supporting:
⚡ Fast embedding generation
💾 Local caching (no re-computation)
🔍 Vector search using FAISS / Cosine Similarity
🌐 FastAPI retrieval API
🧠 Ranking explanation (keyword overlap & scores) 

A clean, modular, production-ready design.
Dataset used: **Text Document Classification Dataset (Kaggle)**  
Converted into multiple `.txt` files.


## 📂 Folder Structure

''' multi-document-embedding-search-engine-with-caching-assignment/
│
├── src/
│   ├── api.py
│   ├── embedder.py
│   ├── search_engine.py
│   ├── cache_manager.py
│   ├── utils.py
│
├── data/                     ← (ignored in Git)
│   └── docs/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
