from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app=Flask(__name__)
model = pickle.load(open("student_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "admin123":
        return redirect(url_for('dashboard'))
    else:
        return "Invalid Username or Password!"
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():

    data = request.form.to_dict()

    df = pd.DataFrame([data])

    prediction = model.predict(df)
    return render_template(
        "index.html",
        prediction_text=f"Predicted Exam Score : {round(prediction[0],2)}"
    )
    
if __name__=="__main__":
    app.run(debug=True)