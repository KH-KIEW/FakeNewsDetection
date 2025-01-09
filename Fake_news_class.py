from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

app = Flask(__name__)

# Import the sai class from the fak_trails module
# Ensure fak_trails.py is in the same directory as this script or in the Python path
from fak_trails import sai

# Initialize the fake_news_detector object
fake_news_detector = sai()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_fake_news():
    if request.method == 'POST':
        text = request.form['text']  # Get the text input from the user

        # Ensure the fake_news24 method is implemented correctly in the sai class
        result = fake_news_detector.fake_news24(text)

        # Return the result on a new page
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
