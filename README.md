# Basic QA Chatbot

A simple question-and-answer chatbot built with Streamlit, LangChain, and Ollama. The application uses the local `llama3.1:8b` model to generate responses.

## Features

- Streamlit web interface
- Local inference through Ollama
- LangChain prompt and output parsing pipeline
- No external API key required for the chatbot model

## Prerequisites

- Python 3.10 or later
- [Ollama](https://ollama.com/) installed and running
- The `llama3.1:8b` model downloaded locally

Download the model with:

```bash
ollama pull llama3.1:8b
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Vickeee1812/Basic-QA-Chatbot.git
cd Basic-QA-Chatbot
```

Create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

Make sure Ollama is running, then start Streamlit:

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit in your browser, usually `http://localhost:8501`.

## Project structure

```text
Basic-QA-Chatbot/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Environment variables

The application loads a `.env` file when present. The `.env` file is ignored by Git, so do not commit secrets to the repository.

## License

This project does not currently specify a license.