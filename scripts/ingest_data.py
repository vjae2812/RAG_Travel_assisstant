import os
import uuid
import chromadb
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import CharacterTextSplitter
from config import DATA_DIR, DB_DIR, COLLECTION_NAME, CHROMA_SETTINGS
from chromadb.config import Settings

os.makedirs(DB_DIR, exist_ok=True)

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client(Settings(**CHROMA_SETTINGS))

# Create collection if not exists
if COLLECTION_NAME not in [c.name for c in client.list_collections()]:
    collection = client.create_collection(name=COLLECTION_NAME)
else:
    collection = client.get_collection(name=COLLECTION_NAME)

def ingest_data(directory_path):
    if collection.count() > 0:
        print("Collection already populated. Skipping ingestion.")
        return

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()

            text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
            documents = text_splitter.split_text(file_content)
            embeddings = model.encode(documents, convert_to_tensor=True)

            for i, doc in enumerate(documents):
                doc_id = str(uuid.uuid4())
                collection.add(
                    ids=[doc_id],
                    documents=[doc],
                    metadatas=[{"filename": filename, "chunk_index": i}],
                    embeddings=[embeddings[i].cpu().numpy().tolist()],
                )
            print(f"Ingested: {filename}")

    # Persist to disk
    client.persist()
