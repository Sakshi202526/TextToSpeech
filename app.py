from flask import Flask, render_template, request

from ai.gemini import analyze_email
from database.db import create_table, save_email


app = Flask(__name__)

# Create SQLite table
create_table()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    email_text = request.form["email"]

    # AI analysis
    result = analyze_email(email_text)

    # Save email and result in SQLite
    save_email(email_text, result)

    # Show result page
    return render_template(
        "result.html",
        email=email_text,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)