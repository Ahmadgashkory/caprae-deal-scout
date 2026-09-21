import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    try:
        if not url.startswith("http"):
            url = "https://" + url
            
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        for script in soup(["script", "style", "header", "footer", "nav"]):
            script.extract()
            
        text = soup.get_text(separator=" ", strip=True)
        return text[:4000] # Token limit safe
        
    except Exception as e:
        return f"Error: {str(e)}"