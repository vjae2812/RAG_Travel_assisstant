from scripts.ingest_data import ingest_data
from scripts.query_engine import find_similar_documents, get_groq_result
from config import DATA_DIR

if __name__ == "__main__":
    print("Ingesting data...")
    ingest_data(DATA_DIR)

    query = input("Ask a travel-related question: ")
    context = find_similar_documents(query)
    answer = get_groq_result(query, context)

    print("\nAnswer:")
    print(answer)
