# 🤖 Multi‑Agent AI Orchestrator

A GenAI web application that analyzes PDF documents using **multiple AI agents** to generate a summary and extract action items.

🌐 Live App: https://ai-document-summarizer-gk8yyg3wqvjywehulvydmw.streamlit.app/

---

## ✨ Features

* Upload PDF documents
* Automatic text extraction & cleaning
* Multi‑agent processing:

  * Planner Agent
  * Summarizer Agent
  * Action‑Item Agent
* Streamlit web interface
* Cloud deployable

---

## 🧠 System Design (Simple)

```
User uploads PDF
        ↓
PDF Reader (extract + clean text)
        ↓
Planner Agent
(decides steps)
        ↓
Summarizer Agent ──► Summary
        ↓
Action Extractor Agent ──► Action Items
        ↓
Results shown on UI
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* HuggingFace Transformers (BART model)
* LangChain (agent structure)
* pypdf
* Git & GitHub

---

## 📌 Why this project

This project demonstrates how **real-world GenAI systems** are built using multiple specialized agents coordinated by an orchestrator instead of a single AI model.

It shows:

* Agent-based architecture
* Orchestration logic
* Practical LLM integration
* System design thinking

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Add your HuggingFace token in `.env`:

```
HUGGINGFACE_API_TOKEN=your_token_here
```

---

## 👩‍💻 Author

Prachi Singh
GitHub: [https://github.com/Prachi57](https://github.com/Prachi57)

---

⭐ If you find this useful, give the repo a star!

