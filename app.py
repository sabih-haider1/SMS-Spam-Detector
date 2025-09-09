from flask import Flask, render_template_string, request
import joblib

# Load trained model
model, vectorizer = joblib.load("spam_model.pkl")

app = Flask(__name__)

# Simple HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SMS Spam Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 400px;
            text-align: center;
        }
        input[type=text] {
            width: 90%;
            padding: 10px;
            margin: 1rem 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            background: #007bff;
            color: white;
            font-size: 1rem;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 1rem;
            font-size: 1.2rem;
            font-weight: bold;
        }
        .ham { color: green; }
        .spam { color: red; }
    </style>
</head>
<body>
    <div class="container">
        <h2>📩 SMS Spam Detector</h2>
        <form method="POST">
            <input type="text" name="message" placeholder="Enter your SMS here..." required>
            <br>
            <button type="submit">Check</button>
        </form>
        {% if prediction %}
            <div class="result {{ prediction }}">
                Prediction: {{ prediction | upper }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        msg = request.form["message"]
        msg_vec = vectorizer.transform([msg])
        pred = model.predict(msg_vec)[0]
        prediction = "spam" if pred == "spam" else "Clear"
    return render_template_string(html_template, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
