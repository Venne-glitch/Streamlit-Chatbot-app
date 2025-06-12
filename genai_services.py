import os
from typing import List
from dotenv import load_dotenv
import google.generativeai as genai
import tiktoken  # make sure this is installed

# Load environment variables
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def call_llm(prompt: str) -> str:
    """
    Calls Gemini Pro with a prompt and returns its response.
    """
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def summarize_text(text: str) -> str:
    prompt = f"Summarize this text concisely:\n\n{text}"
    return call_llm(prompt)


def chunk_text(text: str, chunk_size: int = 100, chunk_overlap: int = 10) -> List[str]:
    """
    Splits text into overlapping chunks using token counts (GPT tokenization).

    Args:
        text: the raw document text
        chunk_size: max token length per chunk
        chunk_overlap: overlapping tokens between chunks

    Returns:
        List of chunked strings
    """
    if not text:
        return []

    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")  # still works for tokenization
    tokens = enc.encode(text)

    chunks = []
    i = 0
    while i < len(tokens):
        chunk_end = min(i + chunk_size, len(tokens))
        chunks.append(enc.decode(tokens[i:chunk_end]))
        i = chunk_end - chunk_overlap if chunk_end < len(tokens) else chunk_end

    return chunks


def answer_with_context(question: str, contexts: List[str]) -> str:
    """
    Answers a question using the provided context chunks.
    """
    context_text = "\n\n".join(contexts)
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context_text}

Question: {question}

Answer:"""
    return call_llm(prompt)
