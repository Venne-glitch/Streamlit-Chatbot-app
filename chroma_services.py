import chromadb
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for required env variable
collection_name = os.getenv("CHROMA_COLLECTION_NAME")
if not collection_name:
    raise ValueError("Missing CHROMA_COLLECTION_NAME in .env file")

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./chrome_db")
collection = chroma_client.get_or_create_collection(name=collection_name)

def ingest_document(docs):
    """
    Ingest documents into ChromaDB (without custom embeddings).

    Args:
        docs (List[str]): List of document chunks

    Returns:
        int: Number of documents ingested
    """
    if not docs:
        print("[DEBUG] No documents to ingest.")
        return 0

    ids = [f"chunk_{i}" for i in range(len(docs))]
    collection.add(documents=docs, ids=ids)
    print(f"[DEBUG] Ingested {len(docs)} chunks into collection '{collection_name}'")
    return len(docs)


def query_documents(query_text, n_results=3):
    """
    Query ChromaDB collection using default embedding search.

    Args:
        query_text (str): Query string
        n_results (int): Number of results to return

    Returns:
        List[str]: List of relevant document chunks
    """
    try:
        results = collection.query(query_texts=[query_text], n_results=n_results)
        
        # ✅ Add these debug logs here:
        print(f"[DEBUG] User query: {query_text}")
        print(f"[DEBUG] Context chunks retrieved: {len(results.get('documents', [[]])[0])}")

        return results.get('documents', [[]])[0]
    except Exception as e:
        print(f"[ERROR] Failed to query ChromaDB: {e}")
        return []

