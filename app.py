from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
import smtplib
from email.message import EmailMessage

#  Create Flask app
app = Flask(__name__)
CORS(app)

#  Database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="portfolio"
)

#  Home route to check server
@app.route("/", methods=["GET"])
def home():
    return "Flask Backend Running"

# Your email credentials
EMAIL_ADDRESS = "rukareashwini@gmail.com"          # your email
EMAIL_PASSWORD = "vtae zunp djhc tlpv" # your app password (not your regular email password)

#  Contact form route
@app.route("/contact-forms", methods=["POST"])
def contact():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        cursor = db.cursor()
        sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, message))
        db.commit()
        cursor.close()

#  Send email notification
        msg = EmailMessage()
        msg['Subject'] = f"New Message from {name}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # send to yourself
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"message": "Message saved and email sent successfully"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

#  Run the app
if __name__ == "__main__":
    app.run(debug=True)
