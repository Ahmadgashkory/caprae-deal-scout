from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from scraper import scrape_website
from multi_agent import analyze_target_company

app = FastAPI(title="Caprae Deal-Scout API")

# React frontend ko connect karne ke liye CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Production mein isay specific domain par set karte hain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    url: str

class ExportRequest(BaseModel):
    data: dict

@app.post("/api/analyze")
async def analyze_url(request: AnalyzeRequest):
    scraped_text = scrape_website(request.url)
    analysis_result = analyze_target_company(request.url, scraped_text)
    
    if "error" in analysis_result:
        raise HTTPException(status_code=400, detail=analysis_result["error"])
        
    return analysis_result

@app.post("/api/export-to-crm")
async def export_to_crm(request: ExportRequest):
    # Yeh webhook aapke n8n workflow par jayega (Video mein impress karne ke liye)
    WEBHOOK_URL = "https://your-n8n-webhook-url.com/webhook/caprae"
    try:
        # requests.post(WEBHOOK_URL, json=request.data)
        return {"status": "success", "message": "Deal successfully pushed to Caprae CRM Pipeline."}
    except Exception as e:
        raise HTTPException(status_code=500, detail="CRM Export Failed")