import smtplib
from email.message import EmailMessage
import logging
from datetime import datetime

def setup_logging(log_file="alerts.log"):
    """
    Configure logging settings.
    """
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def send_email_alert(subject, details, email_config):
    """
    Send a detailed email alert using HTML formatting.
    
    Args:
    - subject (str): Subject of the email.
    - details (dict): Contains detailed information about the threat.
    - email_config (dict): Contains email configurations. Must have "from_email", "to_email", "smtp_server", and "password".
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Construct email body using HTML for better formatting
    body = f"""
    <h1>New Threat Detected</h1>
    <p><strong>Time:</strong> {timestamp}</p>
    <p><strong>Involved IP:</strong> {details.get('ip', 'N/A')}</p>
    <p><strong>Signature Matched:</strong> {details.get('signature', 'N/A')}</p>
    <p><strong>Description:</strong> {details.get('description', 'N/A')}</p>
    """
    
    msg = EmailMessage()
    msg.set_content(body, subtype='html')
    msg['Subject'] = subject
    msg['From'] = email_config["from_email"]
    msg['To'] = email_config["to_email"]

    try:
        with smtplib.SMTP_SSL(email_config["smtp_server"], 465) as server:
            server.login(email_config["from_email"], email_config["password"])
            server.send_message(msg)
    except Exception as e:
        logging.error(f"Failed to send email. Reason: {e}")

def log_alert(alert_message, details):
    """
    Record detailed information about the alert to a log file.
    
    Args:
    - alert_message (str): Basic message to be logged.
    - details (dict): Contains detailed information about the threat.
    """
    log_entry = f"{alert_message}. Involved IP: {details.get('ip', 'N/A')}. Signature: {details.get('signature', 'N/A')}. Description: {details.get('description', 'N/A')}."
    logging.info(log_entry)

def print_alert(alert_message, details):
    """
    Print detailed alert information to the console.
    
    Args:
    - alert_message (str): Basic message to be printed.
    - details (dict): Contains detailed information about the threat.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] ALERT: {alert_message}. Involved IP: {details.get('ip', 'N/A')}. Signature: {details.get('signature', 'N/A')}.")

# Initialize logging for the module upon import.
setup_logging()