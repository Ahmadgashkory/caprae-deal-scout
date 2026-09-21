# Caprae Deal-Scout Platform
**Enterprise-Grade Autonomous M&A Intelligence Engine**

Caprae Deal-Scout is a high-performance, agentic workflow system engineered specifically for the Mergers & Acquisitions (M&A) deal-flow process. Designed to streamline target evaluation, it deploys a multi-agent AI architecture to autonomously scrape target data, analyze market positioning, and synthesize executive-ready investment memos in real-time.

## 🚀 Core Capabilities
* **Intelligent Data Extraction:** Robust scraping mechanism designed to bypass basic bot-protection and extract high-value corporate data.
* **Agentic AI Architecture:** 
  * 🕵️‍♂️ **Market Researcher Agent:** Dynamically queries live market data to establish competitive context.
  * 📊 **Financial Analyst Agent:** Evaluates structural data to output a proprietary AI-Readiness score and identify primary market competitors.
  * 🧠 **Strategic Director Agent:** Synthesizes raw data streams into a cohesive, Caprae-specific Investment Memo.
* **Premium Glassmorphism UI:** A sleek, high-fidelity dark-mode dashboard reflecting modern SaaS standards.
* **Workflow Automation Ready:** Integrated webhook architecture allowing seamless, 1-click push functionality to CRM pipelines (e.g., n8n, Airtable).

## 🛠️ Technical Stack
* **Backend Engine:** FastAPI (Python), LangChain, Pydantic, RESTful API architecture.
* **AI & Data Models:** OpenAI GPT-4o-mini (Structured Outputs), Tavily Live Search API.
* **Frontend Interface:** React.js, Vite, Tailwind CSS (Glassmorphism UI), Lucide Icons, Axios.

## ⚙️ Local Deployment Guide

The platform is divided into a decoupled backend API and a React frontend. Follow these steps to initialize the environment locally.

### 1. Initialize the FastAPI Backend
```bash
# Navigate to the root directory
python -m venv .venv

# Activate the virtual environment
source .venv/Scripts/activate  # For Windows
# source .venv/bin/activate    # For macOS/Linux

# Install backend dependencies
pip install -r requirements.txt

# Create environment variables file
echo "OPENAI_API_KEY=your_key_here" > .env
echo "TAVILY_API_KEY=your_key_here" >> .env

# Launch the Uvicorn ASGI server
uvicorn main:app --reload
The API will be accessible at http://127.0.0.1:8000/docs via Swagger UI.

2. Initialize the React Dashboard
# Navigate to the frontend directory
cd frontend

# Install Node modules
npm install

# Build and serve the frontend
npm run dev
The Dashboard will be live at http://localhost:5173/

🎯 Strategic Objective
Developed exclusively for Caprae Capital. This prototype demonstrates the immediate value of integrating applied AI agents, responsive modern UI engineering, and automated workflows into high-stakes financial intelligence.

Developed by Muhammad Ahmad
