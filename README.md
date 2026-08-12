<div align="center">
  <h1>🔭 Multi-Agent Researcher</h1>
  <p><strong>A team of autonomous AI agents that research, analyze, and write comprehensive reports.</strong></p>
</div>

## 🚀 Overview
The Multi-Agent Researcher is an advanced AI system powered by LangGraph. It orchestrates a "crew" of specialized agents (Searcher, Analyst, Writer, Critic) that autonomously traverse the web, digest information, and collaborate to produce high-quality, cited research reports on any given topic.

## ✨ Features
- **LangGraph Orchestration:** Complex stateful agent workflows with cyclical graphs and conditional edges.
- **Autonomous Web Search:** Uses Tavily API to scrape and synthesize information from academic and live web sources.
- **Self-Correction:** The Critic agent reviews drafts for factual accuracy and bias before final output.
- **Dynamic Formatting:** Export reports as Executive Summaries, Academic Papers, or Blog Posts.

## 🛠️ Tech Stack
- **Graph Framework:** [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/)
- **LLM Backbone:** GPT-4o
- **Search API:** Tavily Search
- **Frontend UI:** [Streamlit](https://streamlit.io/)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad08-dot/multi-agent-researcher.git
   cd multi-agent-researcher
   ```

2. **Install dependencies:**
   ```bash
   pip install langgraph langchain tavily-python streamlit
   ```

3. **Configure Environment:**
   Create a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   ```

4. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📄 License
This project is licensed under the MIT License.
