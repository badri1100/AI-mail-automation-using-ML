import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email account credentials
sender_email = "badrinathbhandage@gmail.com"
sender_password = "gyxr ohtt wvaj ttwc"

# Read email addresses from CSV file
def get_email_list(csv_file):
    email_list = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            email_list.append(row['email'])
    return email_list

# Send email function
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

# Main function to send bulk emails
def send_bulk_emails(csv_file, subject, body):
    email_list = get_email_list(csv_file)
    for email in email_list:
        send_email(email, subject, body)

# Usage
if __name__ == "__main__":
    csv_file = './hello.csv'
    subject = 'Test Email'
    body = 'This is a test email sent from a Python script.'
    send_bulk_emails(csv_file, subject, body)
