📧 Spam Email Detector

📌 Project Overview

This project is a Spam Email Detector that classifies emails as spam or ham (not spam) using machine learning. The model is trained on a dataset of emails with labeled categories and utilizes Natural Language Processing (NLP) techniques for text classification.

🔗 Live Demo

https://spam-email-detector-2.onrender.com/

🔗 GitHub Repository

https://github.com/CodeWithDks/Spam_Email_Detector/tree/master

🏆 Recognition & Certification

This project was developed as part of the Samsung Innovation Campus AI Programs 2024. After successfully completing the program, I received a certificate from Samsung Innovation Campus AI Programs for my work on this project.

🚀 Features

Uses TF-IDF Vectorization for text preprocessing

Trained on a labeled dataset of spam and non-spam emails

Implements Logistic Regression / Naïve Bayes / Random Forest (mention the model used)

Deployed as a web application for real-time email classification


📂 Project Structure

/spam-email-detector
│--templates
│── spam_email_model.pkl
│── app.py
│── requirements.txt
│── README.md

models/ → Contains the trained spam classification model

notebooks/ → Jupyter Notebook for data exploration and training

app.py → Web application to classify emails

requirements.txt → Dependencies needed to run the project


🛠 How to Run Locally

1. Clone the repository:

git clone https://github.com/CodeWithDks/Spam_Email_Detector.git


2. Navigate to the project folder:

cd Spam_Email_Detector


3. Install dependencies:

pip install -r requirements.txt


4. Run the application:

python app.py


5. Open http://127.0.0.1:5000/ in your browser.



📊 Dataset

The dataset contains labeled emails where:

1 = Spam

0 = Ham (Not Spam)

🤖 Machine Learning Model

Accuracy: 94.6

Libraries Used: sklearn, pandas, numpy, Flask, nltk


📢 Future Improvements

Implement deep learning models (LSTMs) for better accuracy

Improve UI for a better user experience

Add real-time email scanning integration


✨ Contributing

Pull requests are welcome! If you’d like to contribute, please fork the repo and create a PR.

📜 License

This project was developed as part of the Samsung Innovation Campus AI Programs 2024. The rights and usage of this project follow the terms outlined by the program.


---

Made with ❤ by Deepak Kumar Singh
