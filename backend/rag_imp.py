from sklearn.metrics.pairwise import cosine_similarity

def retrieve_with_cosine_similarity(query, model, document_embeddings, chunks, top_k=3):
    """
    Retrieves the top-k most relevant chunks for a query using cosine similarity.
    Args:
        query (str): User query.
        model (SentenceTransformer): Embedding model.
        document_embeddings (numpy.ndarray): Array of document embeddings.
        chunks (list): List of document chunks.
        top_k (int): Number of results to return.
    Returns:
        list: Top-k most relevant chunks.
    """
    # Encode the query to get its embedding
    query_embedding = model.encode([query])

    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    # Get the indices of the top-k most similar documents
    top_indices = similarities.argsort()[-top_k:][::-1]

    # Return the top-k most relevant chunks
    return [chunks[i] for i in top_indices]

## Load embeddings and chunks for retrieval, assumed that you save them previously
# document_embeddings = np.load("document_embeddings.npy")
# chunks = np.load("chunks.npy", allow_pickle=True).tolist()