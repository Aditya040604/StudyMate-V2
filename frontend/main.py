import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="PDF Q&A Chatbot",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for black-red modern theme
st.markdown("""
    <style>
    body {
        background-color: #0d0d0d;
        color: #f2f2f2;
    }
    .main {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #e50914;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #b20710;
        color: #fff;
    }
    .chat-history {
        background-color: #262626;
        padding: 15px;
        border-radius: 10px;
        height: 80vh;
        overflow-y: auto;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)


# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Layout with two columns (70% / 30%)
col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.title("📄StudyMate PDF Q&A Chatbot")
    st.write("Ask questions about your PDF and get instant answers!")

    # Upload PDF
    pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

    if pdf_file is not None:
        files = {"file": pdf_file.getvalue()}
        response = requests.post(f"{BACKEND_URL}/upload_pdf", files={"file": pdf_file})
        if response.status_code == 200:
            st.success("✅ PDF uploaded successfully!")
        else:
            st.error("❌ Failed to upload PDF")

    # Input for question
    question = st.text_input("Ask a question from the PDF:")
    if st.button("Get Answer"):
        if pdf_file is None:
            st.warning("Please upload a PDF first.")
        elif question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("⚡ Getting your answer..."):
                payload = {"question": question}
                response = requests.post(f"{BACKEND_URL}/ask_question", data={"question": question})
                if response.status_code == 200:
                    answer = response.json()
                    st.markdown(f"### 📝 Answer:\n{answer}")
                    # Save to history
                    st.session_state.history.append({"q": question, "a": answer})
                else:
                    st.error("❌ Error getting answer")

import html
with col2:
    st.markdown("### 📜 Chat History")

    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[::-1]):
            st.markdown(f"**Q{i+1}:** {item['q']}")
            st.markdown(f"<span style='color:#e50914;'><b>A{i+1}:</b></span> {item['a']}", unsafe_allow_html=True)
            st.divider()
    else:
        st.info("No history yet. Ask something after uploading a PDF.")