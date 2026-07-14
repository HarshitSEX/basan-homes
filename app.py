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

@app.route("/hire-handyman")
def hire_handyman():
    return render_template("hire-handyman.html")

@app.route("/real-estate")
def real_estate():
    return render_template("real-estate.html")


@app.route("/construction")
def construction():
    return render_template("construction.html")

@app.route("/construction/new-homes")
def new_homes():
    return render_template("sub/new-homes.html")

@app.route("/construction/renovations")
def renovations():
    return render_template("sub/renovations.html")

@app.route("/construction/renovations/kitchen")
def kitchen():
    return render_template("sub/detail/kitchen.html")

@app.route("/construction/renovations/bathroom")
def bathroom():
    return render_template("sub/detail/bathroom.html")

@app.route("/construction/renovations/living")
def living():
    return render_template("sub/detail/living.html")

@app.route("/construction/renovations/full-home")
def full_home():
    return render_template("sub/detail/full-home.html")

@app.route("/construction/extensions")
def extensions():
    return render_template("sub/extensions.html")

@app.route("/construction/commercial")
def commercial():
    return render_template("sub/commercial.html")

@app.route("/construction/commercial/office")
def office():
    return render_template("sub/detail/office.html")

@app.route("/construction/commercial/retail")
def retail():
    return render_template("sub/detail/retail.html")

@app.route("/construction/commercial/warehouse")
def warehouse():
    return render_template("sub/detail/warehouse.html")

@app.route("/construction/commercial/development")
def development():
    return render_template("sub/detail/development.html")

@app.route("/construction/knockdown-rebuild")
def knockdown():
    return render_template("sub/knockdown.html")

@app.route("/construction/dual-occupancy")
def dual():
    return render_template("sub/dual.html")

@app.route("/maintenance")
def maintenance():
    return render_template("maintenance-services.html")

@app.route("/maintenance/repairs")
def repairs():
    return render_template("sub/repairs.html")

@app.route("/maintenance/repairs/doors-windows")
def doors_windows():
    return render_template("sub/detail/doors-windows.html")

@app.route("/maintenance/repairs/walls-ceilings")
def walls_ceilings():
    return render_template("sub/detail/walls-ceilings.html")

@app.route("/maintenance/repairs/flooring")
def flooring():
    return render_template("sub/detail/flooring.html")

@app.route("/maintenance/repairs/fencing")
def fencing():
    return render_template("sub/detail/fencing.html")

@app.route("/maintenance/plumbing")
def plumbing():
    return render_template("sub/plumbing.html")

@app.route("/maintenance/electrical")
def electrical():
    return render_template("sub/electrical.html")

@app.route("/maintenance/electrical/power-lighting")
def power_lighting():
    return render_template("sub/detail/power-lighting.html")

@app.route("/maintenance/electrical/safety-switches")
def safety_switches():
    return render_template("sub/detail/safety-switches.html")

@app.route("/maintenance/electrical/solar")
def solar():
    return render_template("sub/detail/solar.html")

@app.route("/maintenance/electrical/inspections")
def inspections():
    return render_template("sub/detail/inspections.html")

@app.route("/maintenance/painting")
def painting():
    return render_template("sub/painting.html")

@app.route("/maintenance/garden")
def garden():
    return render_template("sub/garden.html")

@app.route("/maintenance/garden/garden-maintenance")
def garden_maintenance():
    return render_template("sub/detail/garden-maintenance.html")

@app.route("/maintenance/garden/fencing")
def garden_fencing():
    return render_template("sub/detail/garden-fencing.html")

@app.route("/maintenance/garden/decking")
def decking():
    return render_template("sub/detail/decking.html")

@app.route("/maintenance/garden/concrete-paving")
def concrete_paving():
    return render_template("sub/detail/concrete-paving.html")

@app.route("/maintenance/condition-reports")
def condition_reports():
    return render_template("sub/condition-reports.html")

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
