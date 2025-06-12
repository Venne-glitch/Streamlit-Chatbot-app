import streamlit as st
from markitdown import MarkItDown
from genai_services import chunk_text
from chroma_services import ingest_document  # ✅ FIXED
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    st.error("GOOGLE_API_KEY is not set. Please set it in your .env file.")
    st.stop()

st.title("📄 Document Ingestion & Summarization")

uploaded_file = st.file_uploader(
    "Upload a document (txt, pdf, or any text-based file supported by markitdown)",
    type=["txt", "pdf", "md", "html", "docx"]
)

if uploaded_file:
    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Convert to text using markitdown
    converter = MarkItDown()
    doc_text = converter.convert(tmp_path).text_content
    st.subheader("📃 Document Preview")
    st.text_area("Extracted Text", doc_text, height=200)

    # Chunk and ingest
    with st.spinner("📥 Ingesting document..."):
        try:
            chunks = chunk_text(doc_text)
            ingest_document(chunks)  # ✅ FIXED
            st.success("✅ Document ingested successfully.")
        except Exception as e:
            st.error(f"❌ Ingestion failed: {e}")
