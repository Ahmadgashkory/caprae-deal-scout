import os
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

class DealMemo(BaseModel):
    ai_readiness_score: int = Field(description="Score 1-10 on AI integration potential.")
    priority: str = Field(description="Strictly: High, Medium, or Low")
    competitors: list[str] = Field(description="List of top 3 competitors from search data.")
    investment_memo: str = Field(description="A 4-5 sentence professional investment memo explaining the target's business model, competitive moat, and how Caprae can inject AI to boost their valuation.")

def analyze_target_company(company_url: str, scraped_text: str):
    if "Error" in scraped_text:
        return {"error": "Website scraping failed."}

    # Agent 1: Market Analyst (Tavily Live Search)
    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        search_query = f"What is the business model of {company_url} and who are its main competitors?"
        market_data = tavily.search(query=search_query, search_depth="basic").get("results", [])
    except Exception as e:
        market_data = f"Market search failed: {e}"

    # Agent 2: Deal Strategist (OpenAI)
    llm = ChatOpenAI(temperature=0.2, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    llm_with_tools = llm.with_structured_output(DealMemo)

    prompt = PromptTemplate.from_template(
        "You are a Senior M&A Analyst at Caprae Capital. Caprae acquires SaaS/MaaS businesses and transforms them by integrating AI.\n"
        "Here is the target company data:\n"
        "Website Data: {scraped_text}\n"
        "Live Market Data: {market_data}\n\n"
        "Analyze this data and generate a structured M&A Deal Memo."
    )

    chain = prompt | llm_with_tools
    
    try:
        result = chain.invoke({
            "scraped_text": scraped_text,
            "market_data": str(market_data)[:2000]
        })
        return result.model_dump()
    except Exception as e:
        return {"error": str(e)}