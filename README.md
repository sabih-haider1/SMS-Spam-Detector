📩 SMS Spam Detector

A machine learning project that detects whether a given SMS message is Ham (legit) or Spam using a 54K+ message dataset collected from multiple research sources.
Built with Python, Scikit-learn, and Flask, this project demonstrates how to preprocess text, train a model, and expose predictions through a simple web interface.

🚀 Features

Dataset: 54,000+ labeled SMS messages (Ham/Spam) combined from multiple open-source research corpora.

Machine Learning model: Naive Bayes (scikit-learn).

Text preprocessing with CountVectorizer.

Achieves high accuracy (~98–99%) on test data.

Flask-powered web app with clean HTML interface.

Predict whether a custom SMS is Spam or Ham instantly.

📊 Dataset

Ham messages: ~48,000

Spam messages: ~6,000

Sources: Combined from multiple open datasets used in SMS spam research (e.g. UCI SMS Spam Collection v1, Kaggle repositories, academic spam corpora).

Example format:

ham    What you doing? how are you?  
spam   FreeMsg: Call this number to claim your reward!  

⚙️ Installation & Usage
1. Clone repo
git clone <your-repo-url>
cd sms-spam-detector

2. Create environment & install dependencies
python3 -m venv venv
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows  

pip install -r requirements.txt

3. Train model
python3 train.py


This creates spam_model.pkl (trained Naive Bayes model).

4. Run web app
python3 app.py


Then open browser → http://127.0.0.1:5000

🖼 Screenshots

<img width="1440" height="900" alt="Screenshot 201" src="https://github.com/user-attachments/assets/fda156ca-dc99-4aa9-a9aa-74b6c895a2e8" />
<img width="1440" height="900" alt="Screenshot 200" src="https://github.com/user-attachments/assets/17f92e90-422f-4855-be79-56c5d07c4723" />


🔮 Future Improvements

Try other models (Logistic Regression, SVM, Deep Learning).

Add interactive charts for dataset statistics.

Deploy to Heroku/Render for live demo link.

Build a React frontend to interact with the Flask API.

📜 License

MIT License – free to use and modify.
