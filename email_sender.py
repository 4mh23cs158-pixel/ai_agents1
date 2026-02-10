import smtplib
from email.mime.text import MIMEText

sender = "4mh23cs158@gmail.com"
receiver = "4mh23cs160@gmail.com.com"
password = "your_app_password"

msg = MIMEText("Hello, this is a test email sent from Python.")
msg['Subject'] = "Test Email"
msg['From'] = sender
msg['To'] = receiver

# Connect to Gmail SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Email sent successfully!")
