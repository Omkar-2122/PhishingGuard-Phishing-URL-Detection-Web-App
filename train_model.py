import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import os

def download_phishtank_dataset():
    """Download latest phishing URLs from PhishTank"""
    print("Downloading PhishTank dataset...")
    # You need to register at PhishTank to get an API key
    # url = 'http://data.phishtank.com/data/your-api-key/online-valid.csv'
    # For development, we'll use a small sample dataset
    phishing_urls = [
        'http://malicious-example.com',
        'http://fake-bank.com/login',
        # Add more examples here
    ]
    return pd.DataFrame(phishing_urls, columns=['url'])

def get_legitimate_urls():
    """Get legitimate URLs from trusted sources"""
    print("Collecting legitimate URLs...")
    # For development, we'll use a small sample dataset
    legitimate_urls = [
        'https://www.google.com',
        'https://www.microsoft.com',
        # Add more examples here
    ]
    return pd.DataFrame(legitimate_urls, columns=['url'])

def extract_features(url):
    """Extract features from URL for machine learning"""
    try:
        features = {}
        parsed = urlparse(url)
        
        # URL-based features
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
    except:
        return None

def prepare_dataset():
    """Prepare and combine datasets for training"""
    # Get phishing URLs
    phishing_df = download_phishtank_dataset()
    phishing_df['label'] = 1  # 1 for phishing
    
    # Get legitimate URLs
    legitimate_df = get_legitimate_urls()
    legitimate_df['label'] = 0  # 0 for legitimate
    
    # Combine datasets
    df = pd.concat([phishing_df, legitimate_df], ignore_index=True)
    
    # Extract features
    print("Extracting features...")
    features_list = []
    for url in tqdm(df['url']):
        features = extract_features(url)
        if features:
            features_list.append(features)
    
    # Create feature matrix
    X = pd.DataFrame(features_list)
    y = df['label'][:len(features_list)]
    
    return X, y

def train_model():
    """Train the machine learning model"""
    print("Preparing dataset...")
    X, y = prepare_dataset()
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    print("Training model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    print("\nModel Evaluation:")
    y_pred = model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model
    print("\nSaving model...")
    if not os.path.exists('models'):
        os.makedirs('models')
    joblib.dump(model, 'models/phishing_detector.joblib')
    print("Model saved as 'models/phishing_detector.joblib'")

if __name__ == "__main__":
    train_model()