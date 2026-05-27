from sentence_transformers import CrossEncoder

print("Loading reranker...")

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_results(query, results):

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    pairs = [[query, doc] for doc in documents]

    scores = reranker.predict(pairs)

    combined = list(
        zip(scores, documents, metadatas)
    )

    ranked_results = sorted(
        combined,
        key=lambda x: x[0],
        reverse=True
    )

    return ranked_results