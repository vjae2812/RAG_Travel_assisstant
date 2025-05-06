from sentence_transformers import SentenceTransformer
from config import COLLECTION_NAME, CHROMA_SETTINGS
import chromadb
from chromadb.config import Settings
from groq import Groq

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client(Settings(**CHROMA_SETTINGS))
collection = client.get_collection(name=COLLECTION_NAME)

client = chromadb.Client(chromadb.config.Settings(persist_directory=DB_DIR))  # Load from saved DB
collection = client.get_collection(name=COLLECTION_NAME)  # Load existing collection
def find_similar_documents(query, top_k=10):
    embedding = model.encode([query], convert_to_tensor=True)
    results = collection.query(
        query_embeddings=[embedding[0].cpu().numpy().tolist()],
        n_results=top_k
    )
    docs = results['documents']
    return " ".join([item for sublist in docs for item in sublist])

def get_groq_result(query, context):
    prompt = f"""
You are a Travel Assistant. Based on the user query and the travel context below, answer the question.

User Query:
{query}

Context:
{context}

If an answer is not found in the context, respond with:
"I could not find an answer based on the provided information."
"""

    groq_client = Groq(api_key=GROQ_API_KEY)
    completion = groq_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return completion.choices[0].message.content
