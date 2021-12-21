import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def send_email_encrypted(message_body, subject_line):
# method to send an SSL encrypted email with body and subject line
    msg = EmailMessage()
    msg['Subject'] = subject_line
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'hartmannmatthias7@googlemail.com'
    msg.set_content(message_body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_email(message_body, subject_line):
# method to send an email - non SSL encrypted with body and subject line
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = subject_line
        body = message_body

        msg = f'Subject: {subject_line}\n\n{message_body}'

        smtp.sendmail(EMAIL_ADDRESS, 'hartmannmatthias7@googlemail.com', msg)

