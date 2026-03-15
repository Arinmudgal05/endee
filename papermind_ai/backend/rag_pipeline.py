
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load QA model
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Load vector database
with open("../data/vector_store.pkl", "rb") as f:
    data = pickle.load(f)

chunks = data["chunks"]
embeddings = data["embeddings"]

def search(query, top_k=5):
    query_embedding = embedding_model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    results = [chunks[i] for i in top_indices]
    return results

def ask_question(query):
    context_chunks = search(query)
    context = " ".join(context_chunks)

    response = qa_model(
        question=query,
        context=context
    )

    return response["answer"]
