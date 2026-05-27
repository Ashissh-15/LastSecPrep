import chromadb

from embeddings.embedding_model import generate_embedding
from retrieval.reranker import rerank_results


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="academic_rag"
)


def retrieve_relevant_chunks(query, top_k=5):

    # Query → embedding
    query_embedding = generate_embedding(query)

    # Retrieve larger candidate pool
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=10,
        include=[
            "documents",
            "metadatas"
        ]
    )

    # Rerank results
    reranked_results = rerank_results(
        query,
        results
    )

    # Keep only positive scores
    # filtered_results = [
    #     result
    #     for result in reranked_results
    #     if result[0] > -1
    # ]

    # Return top-k filtered results
    unique_results=[]

    seen=set()

    for score,doc,metadata in reranked_results:

        key=(
            metadata["source"],
            metadata["page"]
        )

        if key not in seen:

            seen.add(key)

            unique_results.append(
                (score,doc,metadata)
            )

    return unique_results[:top_k]