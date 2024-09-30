# Write a program that takes email and message frrom user , and using SMTPLib send that message to all the email in the list

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_emails, subject, message_body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        server.login(sender_email, sender_password)
        
        for recipient in recipient_emails:
            msg['To'] = recipient
            text = msg.as_string()
            server.sendmail(sender_email, recipient, text)
            print(f"Email sent to {recipient}")
            
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

sender_email = input("Enter your email: ")
sender_password = input("Enter your email password: ")
subject = input("Enter the subject: ")
message_body = input("Enter the message: ")
recipient_emails = input("Enter recipient emails separated by commas: ").split(',')

send_email(sender_email, sender_password, recipient_emails, subject, message_body)
