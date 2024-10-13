from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import sklearn
import imblearn

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('spam_email_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email_text']
        input_vectorized = vectorizer.transform([email_text])
        prediction = model.predict(input_vectorized)
        probability = model.predict_proba(input_vectorized)[0]
        
        result = "SPAM" if prediction[0] == 1 else "HAM"
        confidence = probability[1] if prediction[0] == 1 else probability[0]
        
        return jsonify({
            'result': result,
            'confidence': f"{confidence * 100:.2f}%",
            'email_text': email_text
        })

@app.route('/model_info')
def model_info():
    return jsonify({
        'pandas_version': pd.__version__,
        'sklearn_version': sklearn.__version__,
        'imblearn_version': imblearn.__version__,
        'joblib_version': joblib.__version__
    })

if __name__ == '__main__':
    app.run(debug=True)