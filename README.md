# PDF Chatbot with Mistral LLM deployed via Ollama

This is a Streamlit app that allows you to upload a PDF and chat with an AI assistant (powered by Mistral LLM) about its content.

## Features
- Upload any PDF file
- Ask questions about the PDF content
- Get answers from a local LLM (Ollama)

## Requirements
- Python 3.10+
- [Ollama](https://ollama.com/) running locally (default: http://localhost:11434)

## Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd PDFCHATBOT
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make sure Ollama is running locally.

## Usage
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser to [http://localhost:8503](http://localhost:8503)
3. Upload a PDF and start chatting!

## Configuration
- By default, the app connects to Ollama at `http://localhost:11434`. You can change this in `app.py` if needed.

## License
MIT 
