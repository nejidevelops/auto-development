import dbus
import dbus.mainloop.glib
from gi.repository import GLib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email update
def send_email_update(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Handler for session lock/unlock events
def handle_signal(sender, value):
    if value:
        print("Session locked")
        send_email_update("Machine Locked", "Your machine has been locked.", to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)
    else:
        print("Session unlocked")
        send_email_update("Machine Unlocked", "Your machine has been unlocked.", to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)

# Main function to monitor lock events
def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    
    bus.add_signal_receiver(
        handle_signal,
        dbus_interface="org.freedesktop.login1.Session",
        signal_name="Lock"
    )
    bus.add_signal_receiver(
        handle_signal,
        dbus_interface="org.freedesktop.login1.Session",
        signal_name="Unlock"
    )
    
    loop = GLib.MainLoop()
    loop.run()

# Set up your email credentials and recipient
to_email = "recipient@example.com"
from_email = "your_email@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_user = "your_email@example.com"
smtp_password = "your_email_password"

# Start monitoring lock events
if __name__ == "__main__":
    main()
