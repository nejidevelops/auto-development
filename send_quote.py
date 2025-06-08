import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load quotes
with open(os.path.expanduser("/home/neji/Desktop/auto-development/quotes.txt")) as f:
    quotes = f.readlines()
quote = random.choice(quotes).strip()

# Email setup
sender = "newtonombese1@gmail.com"
password = "phcr fhao xkbm hzhm"  # use an app password if using Gmail
recipient = "newtonombese1@gmail.com"

FROM = "Neji"
TO = "newtonombese1@gmail.com"
SUBJECT = "🖥️ Hourly System Status"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = "💡 Your Daily Tech Quote"

msg.attach(MIMEText(quote, "plain"))

# Send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
except Exception as e:
    print("Failed to send email:", e)
