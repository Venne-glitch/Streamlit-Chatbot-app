import streamlit as st
from genai_services import answer_with_context
from chroma_services import query_documents

# --- Page content ---
st.title("🤖 ChatBot QnA")
st.write("Ask a question about your uploaded documents.")

# --- Chat input ---
user_query = st.chat_input("Your question:")

# --- Process query ---
if user_query:
    try:
        with st.spinner("🔍 Searching documents..."):
            context_chunks = query_documents(user_query, n_results=3)
            print(f"[DEBUG] User query: {user_query}")
            print(f"[DEBUG] Context chunks retrieved: {len(context_chunks)}")

        if not context_chunks:
            st.warning("⚠️ No relevant context found for this query.")
        else:
            with st.spinner("🧠 Generating answer..."):
                answer = answer_with_context(user_query, context_chunks)
                print(f"[DEBUG] Generated answer: {answer}")

            # --- Display result ---
            st.markdown("### ✅ Answer:")
            st.success(answer)

    except Exception as e:
        st.error(f"❌ Error: {e}")
        print(f"[ERROR] Exception in chatbot: {e}")
