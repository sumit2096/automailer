import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, recipient_name):
    # SMTP server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_password'

    # Read HTML template
    with open('email_template.html', 'r') as file:
        html_content = file.read()

    # Replace placeholders in HTML template
    html_content = html_content.replace('{{recipient_name}}', recipient_name)
    html_content = html_content.replace('{{link}}', 'https://www.example.com/get-started')

    # Create message
    msg = MIMEMultipart('alternative')
    msg['From'] = smtp_username
    msg['To'] = recipient_email
    msg['Subject'] = 'Welcome to Our Service'

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")

# Example usage
send_email('recipient@example.com', 'John Doe')
