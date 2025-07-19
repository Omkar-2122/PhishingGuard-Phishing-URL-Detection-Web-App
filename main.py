from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
import joblib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import os

app = FastAPI(title="PhishingGuard", description="Real-Time URL Phishing Detection")

# Mount static files
static_path = Path("static")
static_path.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Feature extraction functions
def extract_url_features(url):
    features = {}
    
    # Parse URL
    parsed = urlparse(url)
    
    # Basic URL features
    features['length_url'] = len(url)
    features['length_hostname'] = len(parsed.netloc)
    features['ip_present'] = 1 if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', parsed.netloc) else 0
    features['nb_dots'] = url.count('.')
    features['nb_hyphens'] = url.count('-')
    features['nb_at'] = url.count('@')
    features['nb_qm'] = url.count('?')
    features['nb_and'] = url.count('&')
    features['nb_eq'] = url.count('=')
    features['nb_underscore'] = url.count('_')
    features['nb_tilde'] = url.count('~')
    features['nb_percent'] = url.count('%')
    features['nb_slash'] = url.count('/')
    features['nb_star'] = url.count('*')
    features['nb_colon'] = url.count(':')
    features['https_token'] = 1 if re.findall(r'^https', url) else 0
    
    return features

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scan")
async def scan_url(url: str = Form(...)):
    try:
        # Extract features
        features = extract_url_features(url)
        
        # Convert features to DataFrame
        df = pd.DataFrame([features])
        
        # TODO: Load and use ML model for prediction
        # For now, return dummy result
        result = {
            "url": url,
            "is_phishing": False,  # This will be replaced with actual model prediction
            "confidence": 0.95,    # This will be replaced with actual confidence score
            "features": features
        }
        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)