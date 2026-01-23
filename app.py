import streamlit as st
from orchestrator import Orchestrator
from utils.pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="Multi-Agent AI Orchestrator")

st.title("🤖 Multi-Agent AI Document Analyzer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading document..."):
        text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Document"):
        with st.spinner("Running AI agents..."):
            orchestrator = Orchestrator()
            result = orchestrator.run(text)

        st.subheader("📄 Summary")
        st.write(result.get("summary", ""))

        st.subheader("✅ Action Items")
        st.write(result.get("action_items", ""))
