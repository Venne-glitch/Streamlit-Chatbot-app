import streamlit as st

st.set_page_config(page_title="Document Ingest and Summarization", layout="wide", initial_sidebar_state="expanded")

ingest_page = st.Page("pages/1_ingest_page.py", title = "ingest")
chatbot_page = st.Page("pages/2_chatbot_page.py", title = "chatbot")

pg = st.navigation([
    ingest_page,
    chatbot_page,
])

pg.run()
