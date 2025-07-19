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

## 📁 Project Structure

PhishingGuard/
├── app.py # Flask backend application
├── train_model.py # Script to train and save the ML model
├── model.pkl # Trained model file
├── phishing_dataset.csv # Dataset used for training
├── requirements.txt # List of required Python packages
├── static/
│ └── style.css # CSS styles
├── templates/
│ └── index.html # Frontend UI for the app
└── README.md # Project documentation

yaml
Always show details

Copy

---


## 💻 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Omkar-2122/PhishingGuard-Phishing-URL-Detection-Web-App.git
cd PhishingGuard-Phishing-URL-Detection-Web-App
2. Create and Activate a Virtual Environment (Optional but Recommended)
bash
Always show details

Copy
python -m venv venv
# Activate:
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Required Packages
bash
Always show details

Copy
pip install -r requirements.txt
4. Train the ML Model (Skip if model.pkl already exists)
bash
Always show details

Copy
python train_model.py
5. Run the Flask App
bash
Always show details

Copy
python app.py
Open your browser and go to: http://127.0.0.1:5000

📦 Example requirements.txt
txt
Always show details

Copy
Flask
pandas
numpy
scikit-learn
joblib
You can generate this with:

bash
Always show details

Copy
pip freeze > requirements.txt
🧠 Dataset & Model
Dataset: Kaggle – Phishing Site URLs

Model: Random Forest Classifier (model.pkl)

Training Script: train_model.py

👨‍💻 Author
Omkar Chavan
🎓 Final Year B.Tech – CSE | Cybersecurity Enthusiast
📧 Email: omkarchavan2122@gmail.com
🌐 GitHub: Omkar-2122

⚠️ Disclaimer
This tool is created for educational and demonstration purposes only.
Do not rely on it as the only security solution. Always follow best practices when handling URLs and web security.
