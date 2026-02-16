# 📚 Literature Review Assistant (AutoGen + Streamlit)

An **AI-powered literature review system** that automatically searches **arXiv research papers** based on a user-provided topic and generates a **clear, structured summary** using a multi-agent workflow built with **Microsoft AutoGen**.

The project features:

* 🔎 **Research Agent** – finds relevant arXiv papers for a given topic
* 🧠 **Summarization Agent** – synthesizes findings into a concise literature review
* ⚡ **Real-time streaming UI** – built with **Streamlit**
* 🤖 **Local or remote LLM support** – compatible with **Ollama / OpenAI-style models**

---

## 🏗️ Architecture

```
User Query → Research Agent → arXiv Papers → Summarization Agent → Final Review → Streamlit UI
```

### Components

* **AutoGen Agents**

  * Research agent performs paper discovery
  * Summarizer agent produces structured insights
* **arXiv Tool**

  * Retrieves title, authors, date, abstract, and PDF link
* **Streaming Runtime**

  * Async conversation streamed live to the UI
* **Streamlit Frontend**

  * Interactive topic input and paper count selection

---

## 🚀 Features

* Multi-agent collaboration using **AutoGen**
* Topic-based **arXiv paper retrieval**
* **Concise literature summaries**
* **Async real-time streaming** responses
* Clean **chat-style Streamlit interface**


---

## 📂 Project Structure

```
Literature_Review
│   Architecture.png
│   LICENSE
│   main.py
│   README.md
│   Streamlit_Frontend.py
│
├───Agents
│   │   Research_agent.py
│   │   Summarizer_agent.py
│   │
│   
│
├───Models
│   │   ollama_model_client.py
│   │
│   
├───prompts
│   │   research_prompt.py
│   │   summary_prompt.py
│   │
│   
├───teams
│   │   team_round_robin.py
│   
│   
├───tools
│   │   Arvix_tool.py

```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/literature-review-assistant.git
cd literature-review-assistant
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run ./Streamlit_Frontend.py
```

Then open the local URL shown in the terminal.

---

## 🧪 Example Usage

1. Enter a **research topic** (e.g., *AI Agents in Software Engineering*)
2. Choose the **number of papers**
3. Click **Search**
4. Watch the **multi-agent discussion stream live**
5. Receive a **final summarized literature review**

---

## 🧰 Tech Stack

* **Python**
* **Microsoft AutoGen**
* **Streamlit**
* **arXiv API**
* **Ollama / OpenAI-compatible LLMs**
* **AsyncIO streaming**

---

## 📌 Future Improvements

* Citation formatting (APA/IEEE)
* Export to **PDF / Markdown**
* Multi-topic comparison
* Vector database + RAG memory
* UI for browsing individual papers

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ⭐ Acknowledgements

* Microsoft **AutoGen**
* **arXiv** research database
* Open-source LLM ecosystem

---

**Built for exploring automated scientific literature review using collaborative AI agents.**
