import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("ℹ️ About This App")
st.write("""
This is a Streamlit-based application that allows you to:
- Ingest documents
- Ask questions using a RAG (Retrieval-Augmented Generation) chatbot
""")
