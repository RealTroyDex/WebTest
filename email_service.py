import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SENDER_EMAIL = 'noreply@example.com'
SENDER_PASSWORD = 'your_password'

def send_activation_email(email, activation_code):
    message = f"Hello!\n\nThank you for registering. Your activation code is: {activation_code}\n\nPlease use this code to activate your account."
    msg = MIMEText(message)
    msg['Subject'] = 'Account Activation'
    msg['From'] = SENDER_EMAIL
    msg['To'] = email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
