import threading
import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'operations@basanhomes.com.au'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'folkirfdbkwzpsqw')
app.config['MAIL_DEFAULT_SENDER'] = 'operations@basanhomes.com.au'

mail = Mail(app)

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            print(f"Email error: {e}")



@app.route("/robots.txt")
def robots():
    return app.send_static_file('robots.txt')

@app.route("/sitemap.xml")
def sitemap():
    return app.send_static_file('sitemap.xml')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False
    error = False
    if request.method == "POST":
        name     = request.form.get("name")
        email    = request.form.get("email")
        phone    = request.form.get("phone")
        service  = request.form.get("service")
        suburb   = request.form.get("suburb")
        budget   = request.form.get("budget")
        timeline = request.form.get("timeline")
        message  = request.form.get("message")
        try:
            msg = Message(
                subject=f"New Enquiry from {name} — Basan Homes",
                recipients=["operations@basanhomes.com.au"],
                body=f"""
New enquiry from Basan Homes website:

Name:     {name}
Email:    {email}
Phone:    {phone}
Suburb:   {suburb}
Service:  {service}
Budget:   {budget}
Timeline: {timeline}

Message:
{message}
                """
            )
            threading.Thread(target=send_async_email, args=(app, msg)).start()
            sent = True
        except Exception as e:
            print(f"Email error: {e}")
            error = True
    return render_template("contact.html", sent=sent, error=error)

if __name__ == "__main__":
    app.run(debug=True)
