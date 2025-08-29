
import pdf_reader as pdf_reader
import embedding_generator as embedding_generator
import rag_imp as rag_imp
import generate_ai as generate_ai
import numpy as np



api_key = "AIzaSyCgoCdWg6vbDNsTrhogULWUzwrEUmCZdtg"

def process_pdf(pdf_path):
    pdf_text = pdf_reader.extract_text_from_pdf(pdf_path)
    chunks = embedding_generator.split_text(pdf_text)

    document_embeddings = embedding_generator.model.encode(chunks, show_progress_bar=False)

    np.save("document_embeddings.npy", document_embeddings)
    np.save("chunks.npy", np.array(chunks))
    return "pdf processed successfully"

def ask_question(input):
    document_embeddings = np.load("document_embeddings.npy")
    chunks = np.load("chunks.npy", allow_pickle=True).tolist()

    retrieved_chunks = rag_imp.retrieve_with_cosine_similarity(input, embedding_generator.model, document_embeddings, chunks)
    context = "\n".join(retrieved_chunks)

    prompt = f"""Context information is below.
---------------------
{context}
---------------------
Given the context information above I want you to think step by step to answer the query in a crisp manner, in case you don't know the answer say 'I don't know!'.
Query: {input}
Answer: """

    response = generate_ai.generate_response(prompt, api_key)
    return (f"{response['candidates'][0]['content']['parts'][0]['text']}")

# def main(input, pdf_path):
#     pdf_text = pdf_reader.extract_text_from_pdf(pdf_path)
#     chunks = embedding_generator.split_text(pdf_text)
#     document_embeddings = embedding_generator.model.encode(chunks, show_progress_bar=False)
#     np.save("document_embeddings.npy", document_embeddings)
#     np.save("chunks.npy", np.array(chunks))
#     document_embeddings = np.load("document_embeddings.npy")
#     chunks = np.load("chunks.npy", allow_pickle=True).tolist()

#     retrieved_chunks = rag_imp.retrieve_with_cosine_similarity(input, embedding_generator.model, document_embeddings, chunks)
#     context = "\n".join(retrieved_chunks)

#     prompt = f"""Context information is below.
# ---------------------
# {context}
# ---------------------
# Given the context information above I want you to think step by step to answer the query in a crisp manner, in case you don't know the answer say 'I don't know!'.
# Query: {input}
# Answer: """

#     response = generate_ai.generate_response(prompt, api_key)
#     return (f"Bot: {response['candidates'][0]['content']['parts'][0]['text']}")
    

# print(main("simple overview?", "new.pdf"))