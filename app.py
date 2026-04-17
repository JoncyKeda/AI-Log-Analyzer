import streamlit as st
from utils.parser import extract_errors
from utils.analyzer import analyze_logs

st.set_page_config(page_title="AI Log Analyzer", layout="wide")

st.title("🧾 AI Log Analyzer")

uploaded_file = st.file_uploader("Upload Log File", type=["txt"])

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8")

    errors = extract_errors(logs)

    st.subheader("🚨 Detected Errors")
    st.write(errors)

    if st.button("Analyze with AI"):
        analysis = analyze_logs(errors)

        st.subheader("🧠 AI Analysis")
        st.write(analysis)
