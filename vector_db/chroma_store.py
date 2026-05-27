import chromadb

from embeddings.embedding_model import generate_embedding


client = chromadb.PersistentClient(path="chroma_db")


collection = client.get_or_create_collection(
    name="academic_rag"
)


def store_documents(documents):

    for index, doc in enumerate(documents):

        embedding = generate_embedding(doc["text"])

        collection.add(
            ids=[f"doc_{index}"],

            embeddings=[embedding],

            documents=[doc["parent_text"]],

            metadatas=[{
                "source": doc["source"],
                "page": doc["page"],
                "chunk_id": doc["chunk_id"]
            }]
        )