import sys
import streamlit as st
import PyPDF2
import io
import requests

class OllamaAPI:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        
    def generate_response(self, prompt, model="mistral"):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json()['response']
        return "Error generating response"

ollama = OllamaAPI()

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for i, page in enumerate(pdf_reader.pages):
        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        except Exception as e:
            print(f"Warning: Could not extract text from page {i}: {e}")
            continue
    return text

st.title("PDF ChatBot With Ollama Mistral")
st.write("Python executable:", sys.executable)

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if 'pdf_content' not in st.session_state:
    st.session_state.pdf_content = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file is not None:
    if st.session_state.pdf_content is None:
        with st.spinner("Processing PDF..."):
            st.session_state.pdf_content = extract_text_from_pdf(uploaded_file)
        st.success("PDF processed successfully!")

if st.session_state.pdf_content is not None:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    if question := st.chat_input("Ask a question about your PDF"):
        with st.chat_message("user"):
            st.write(question)
        st.session_state.chat_history.append({"role": "user", "content": question})
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                prompt = f"Given the following PDF content:\n{st.session_state.pdf_content}\n\nAnswer this question: {question}"
                response = ollama.generate_response(prompt)
                st.write(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
else:
    st.info("Please upload a PDF file to start chatting.") 