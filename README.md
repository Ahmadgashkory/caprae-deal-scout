# 🐐 Caprae Deal-Scout 
**Enterprise-Grade Agentic M&A Intelligence Platform**

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

Caprae Deal-Scout is a high-performance, autonomous workflow engine designed specifically to supercharge the Mergers & Acquisitions (M&A) pipeline. By inputting a target SaaS company's URL, the system orchestrates a multi-agent AI workforce to instantly scrape data, analyze market readiness, and generate a comprehensive investment memo.

---

## 🚀 The Multi-Agent Architecture
Instead of relying on a single AI prompt, Deal-Scout deploys three specialized, collaborating agents:

1. **🕵️‍♂️ The Researcher Agent:** Bypasses basic bot protection to extract core web data and utilizes the Tavily API for live market context.
2. **📊 The Analyst Agent:** Processes raw data to calculate a standardized `AI-Readiness Score` and identifies real-time market competitors.
3. **🧠 The Strategist Agent:** Synthesizes findings into a professional, Caprae-specific Investment Memo, ready for executive review.

## ✨ Core Features
- **Zero-Click Intelligence:** Enter a URL and get a complete deal profile in seconds.
- **Glassmorphism UI:** A stunning, modern React dashboard utilizing Tailwind CSS for an immersive user experience.
- **Live Competitor Mapping:** Automatically detects and lists direct market rivals.
- **CRM Pipeline Ready:** Built-in "Push to CRM" mock functionality to demonstrate seamless integration with existing enterprise workflows.

## 🛠️ Technical Stack
* **Backend:** FastAPI, Python, LangChain, OpenAI (GPT-4o-mini), Tavily Search API.
* **Frontend:** React.js, Vite, Tailwind CSS, Lucide React Icons, Axios.
* **Paradigm:** RESTful API communication, asynchronous processing, and prompt-engineered agent routing.

---

## ⚙️ Local Development Setup

### 1. Initialize the Backend
```bash
# Navigate to the root directory
python -m venv .venv
source .venv/Scripts/activate # For Windows
pip install -r requirements.txt

# Create a .env file
