# 🧳 RAG-Based Travel Assistance Chatbot

This project is a **Retrieval-Augmented Generation (RAG)** based chatbot that helps users with travel-related queries using contextual information retrieved from Wikitravel.

## 🔧 Features

- Scrapes travel pages via [Jina AI](https://r.jina.ai)
- Stores data in [ChromaDB]
- Embeds text using `SentenceTransformers`
- Performs similarity search and answers using `Groq` (LLaMA 3)

## 🚀 Project Structure

rag-travel-assistant/
│
├── data/                            # Stores raw and processed travel text files
│
├── db/                              # Persistent vector store (ChromaDB)
│
├── scripts/                         # All Python scripts
│   ├── 01_fetch_data.py             # Fetch travel data from URLs using curl
│   ├── 02_ingest_data.py            # Ingest and embed text files into ChromaDB
│   ├── 03_query_engine.py           # Similarity search and LLM response
│
├── .gitignore                       # Files/folders Git should ignore
├── README.md                        # Project overview and instructions
├── requirements.txt                 # Python dependencies
├── config.py                        # Configuration (e.g., paths, API keys)
└── run.py                           # Entrypoint to run the complete pipeline
