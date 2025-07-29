#instalation 
uv add openai-agents python-dotenv chainlit
#run command
uv run chainlit run main.py -w
# 🤖 Q/A ChatBot Agent using Chainlit + Gemini API

This is a simple, interactive Q\&A chatbot built using [Chainlit](https://www.chainlit.io/) and Google's [Gemini API](https://ai.google.dev/), integrated using OpenAI-compatible API structure.

> 💡 The chatbot provides helpful and human-like responses using Gemini 2.0 Flash model.

---

## 🚀 Features

* 🔗 Gemini API (OpenAI-Compatible) integration
* 💬 Conversational memory (chat history)
* 🤖 Agent system with instructions and config
* 🧠 Built using Chainlit for an interactive frontend
* ⚙️ Async handling with environment config

---

## 📁 Folder Structure

```
Q-A-chatBot-agnent/
│
├── agents/
│   ├── __init__.py
│   └── run.py              # Contains RunConfig and Runner logic
│
├── .chainlit/
│   ├── config.toml
│   └── translations/
│
├── main.py                 # Chatbot logic with chat handlers
├── chainlit.md             # (Optional) Chainlit documentation
├── .env                    # Gemini API key (keep this secret)
├── .gitignore              # Ignore .env and cache
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/seher873/Q-A-chatBot-agnent.git
cd Q-A-chatBot-agnent
```

### 2. Install Dependencies

Make sure Python 3.9+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Set Up Your Environment Variables

Create a `.env` file in the root folder and add your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the App

```bash
chainlit run main.py
```

It will open a local web interface at `http://localhost:8000`.

---

## 📸 Preview

> Coming Soon! (Add a screenshot of your app here)

---

## ✅ Todo

* [ ] Add user authentication
* [ ] Add export chat feature
* [ ] Improve UI/UX
* [ ] Deploy online (e.g. Streamlit Cloud or Render)

---

## 🙏 Acknowledgments

* [Chainlit](https://github.com/Chainlit/chainlit)
* [Gemini API Docs](https://ai.google.dev/gemini-api/docs/openai)
* OpenAI-style SDK compatibility

---

## 📜 License

This project is for educational/demo purposes. Add a license if you plan to share/distribute officially.

---

#gitignore file ....command,,
New-Item -Path . -Name ".gitignore" -ItemType "File"

