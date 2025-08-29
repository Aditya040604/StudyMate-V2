from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Split text into chunks
def split_text(text, chunk_size=500):
    """
    Splits text into smaller chunks of specified size.
    Args:
        text (str): The text to split.
        chunk_size (int): Size of each chunk.
    Returns:
        list: A list of text chunks.
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# chunks = split_text(pdf_text)

# Generate embeddings for each chunk
# document_embeddings = model.encode(chunks, show_progress_bar=True)

## Save embeddings and chunks for retrieval, if you want to use it later
# np.save("document_embeddings.npy", document_embeddings)
# np.save("chunks.npy", np.array(chunks))