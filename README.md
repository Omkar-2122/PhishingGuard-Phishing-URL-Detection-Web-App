# PhishingGuard - Real-Time URL Phishing Detection

PhishingGuard is a modern web application that uses machine learning to detect potential phishing URLs in real-time. Built with Python FastAPI for the backend and a responsive HTML/CSS frontend, it provides instant feedback on URL safety.

## Features

- Real-time URL scanning and analysis
- Machine learning-based phishing detection
- Modern, responsive user interface
- Detailed URL feature analysis
- Fast and efficient processing

## Technology Stack

- **Backend**: Python FastAPI
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: scikit-learn
- **Database**: SQLite (optional)
- **Other Tools**: BeautifulSoup4, Pandas, NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PhishingGuard.git
cd PhishingGuard
```

2. Create a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Train the machine learning model (optional - if you want to use your own model):
```bash
python train_model.py
```

2. Start the application:
```bash
python main.py
```

3. Open your web browser and navigate to:
```
http://localhost:8000
```

## Project Structure

```
PhishingGuard/
├── main.py              # FastAPI application
├── train_model.py       # ML model training script
├── requirements.txt     # Project dependencies
├── static/
│   └── styles.css      # CSS styles
├── templates/
│   └── index.html      # HTML template
└── models/             # Directory for ML models
```

## How It Works

1. **URL Feature Extraction**: When a URL is submitted, the application extracts various features such as:
   - URL length
   - Domain name characteristics
   - Special character frequency
   - Protocol type
   - And more...

2. **Machine Learning Analysis**: These features are analyzed by a trained Random Forest model to determine if the URL is potentially malicious.

3. **Real-time Results**: Results are instantly displayed with:
   - Safety status
   - Confidence score
   - Detailed feature analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. While it can help identify potential phishing URLs, it should not be the sole factor in determining URL safety. Always exercise caution when clicking on unknown links.