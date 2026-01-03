import streamlit as st
import tempfile
from rag_backend import build_rag_chain, ask_rag


# PAGE CONFIG

st.set_page_config(
    page_title="Chat with your data",
    layout="wide"
)





# CSS
st.markdown("""
<style>
.stChatMessage {
    color: black !important;
}
.stApp {
    background-color: #8080c0;
    color: black;
}
.header {
    padding: 10px 30px;
    border-bottom: 1px solid #e6e6e6;
}
.center {
    text-align: center;
    margin-top: 60px;
}
.subtitle {
    color: #666;
    font-size: 18px;
}



</style>
""", unsafe_allow_html=True)


# HEADER

st.markdown("""
<div class="header">
    <b>Upload | Search | From your Data</b>
</div>
""", unsafe_allow_html=True)


# SESSION STATE INIT

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload a TXT document",
    type=["txt"]
)

if uploaded_file and st.session_state.rag_chain is None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    with st.spinner("Indexing document..."):
        st.session_state.rag_chain = build_rag_chain(file_path)

    st.success("✅ Document indexed successfully")

elif not uploaded_file:
    st.info("📄 Upload a document to enable search")


# MAIN TITLE

st.markdown("""
<div class="center">
    <h1>Chat with your data</h1>
    <div class="subtitle">Ask questions based only on your uploaded document</div>
</div>
""", unsafe_allow_html=True)


# CHAT HISTORY

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# CHAT INPUT 

prompt = st.chat_input(
    "Upload a document to start asking questions",
    disabled=st.session_state.rag_chain is None
)


# ASK RAG

if prompt and st.session_state.rag_chain:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Searching document..."):
            answer = ask_rag(st.session_state.rag_chain, prompt)
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
