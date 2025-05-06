# config.py
GROQ_API_KEY = "your_API"
DATA_DIR = "./data/"
DB_DIR = "./db/"
COLLECTION_NAME = "thailand_travel_data"

CHROMA_SETTINGS = {
    "chroma_db_impl": "duckdb+parquet",
    "persist_directory": DB_DIR
}
