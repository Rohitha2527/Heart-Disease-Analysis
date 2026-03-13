from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Story Page
@app.route("/story")
def story():
    return render_template("story.html")


# Team Page
@app.route("/team")
def team():
    return render_template("team.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Risk Checker Page
@app.route("/risk")
def risk():
    return render_template("risk.html")


# Risk Calculation (Python Logic - No ML)
@app.route("/calculate_risk", methods=["POST"])
def calculate_risk():

    age = int(request.form["age"])
    gender = request.form["gender"]
    diabetes = request.form["diabetes"]
    cholesterol = int(request.form["cholesterol"])
    blood_pressure = int(request.form["blood_pressure"])
    heart_rate = int(request.form["heart_rate"])

    risk_score = 0

    # Age condition
    if age >= 50:
        risk_score += 1

    # Gender condition
    if gender == "male":
        risk_score += 1

    #diabetes condition
    if diabetes == "yes":
        risk_score += 2

    # Cholesterol condition
    if cholesterol >= 240:
        risk_score += 2

    # Blood Pressure condition
    if blood_pressure >= 140:
        risk_score += 2

    # Heart Rate condition
    if heart_rate < 100:
        risk_score += 1

    # Risk Result
    if risk_score >= 6:
        result = "High Risk of Heart Disease"
    elif risk_score >= 3:
        result = "Moderate Risk of Heart Disease"
    else:
        result = "Low Risk of Heart Disease"

    return render_template("risk.html", prediction=result)


# Run Server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)




