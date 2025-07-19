# 🛡️ PhishingGuard – Real-Time Phishing URL Detection Web App

PhishingGuard is a real-time web application that detects and classifies phishing URLs using a machine learning model. The application provides a clean, simple interface for users to input URLs and check their safety using a trained Random Forest classifier.

---

## 🚀 Features

- ✅ Detects whether a URL is phishing or legitimate  
- 🤖 Built using machine learning (Random Forest)  
- 🌐 Flask-based web interface  
- 📊 Supports model retraining with new datasets  
- ⚡ Fast and lightweight for quick predictions  

---

## 🛠️ Tech Stack

| Category         | Technology                                |
|------------------|--------------------------------------------|
| **Languages**     | Python, HTML, CSS                         |
| **Framework**     | Flask                                     |
| **Libraries**     | scikit-learn, pandas, numpy, joblib       |
| **ML Algorithm**  | Random Forest Classifier                  |
| **Frontend**      | HTML5, CSS3 (Bootstrap optional)          |
| **Database**      | Not required (can use SQLite optionally)  |

---

PhishingGuard/

├── app.py                 # Flask backend application  
├── train_model.py         # Script to train and save the ML model  
├── model.pkl              # Trained model file  
├── phishing_dataset.csv   # Dataset used for training  
├── requirements.txt       # List of required Python packages  
├── static/  
│   └── style.css          # CSS styles  
├── templates/  
│   └── index.html         # Frontend UI for the app  
└── README.md              # Project documentation


---


## ⚙️ How to Run

```bash
# Clone repo
git clone https://github.com/Omkar-2122/PhishingGuard-Phishing-URL-Detection-Web-App.git
cd PhishingGuard-Phishing-URL-Detection-Web-App

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Train model (only once)
python train_model.py

# Run the app
python app.py
Visit: http://127.0.0.1:5000

📦 Tech Stack
Python, Flask

Scikit-learn, Pandas

HTML/CSS

👨‍💻 Author
Omkar Chavan
🎓 B.Tech – CSE | Cybersecurity Enthusiast
📧 omkarchavan2122@gmail.com
🔗 GitHub: Omkar-2122

⚠️ Disclaimer
For educational purposes only.
Do not rely on this tool as a complete security solution.

---

Let me know if you want it as a downloadable `.md` or `.pdf`.
