# send_email.py
import smtplib
from email.mime.text import MIMEText
import sys

# Read message from stdin
body = sys.stdin.read()

# Email config
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = "newtonombese1@gmail.com"
PASSWORD = "phcr fhao xkbm hzhm"  # Use Gmail App Password if 2FA is enabled

FROM = USERNAME
TO = "newtonombese1@gmail.com"
SUBJECT = "🖥️ Hourly System Status"

# Compose and send
msg = MIMEText(body)
msg["From"] = FROM
msg["To"] = TO
msg["Subject"] = SUBJECT

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM, [TO], msg.as_string())
    server.quit()
except Exception as e:
    print("Error sending email:", e)
