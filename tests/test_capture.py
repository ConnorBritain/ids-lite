import loguru
import smtplib
from email.mime.text import MIMEText

# Configurations
ALERTS_LOG_FILE = 'logs/alerts_{time}.log'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
ALERT_EMAIL_RECIPIENT = 'recipient@example.com'

# Initialize the logger for alerts
loguru.logger.add(ALERTS_LOG_FILE, rotation="1 day", retention="10 days")

class AlertHandler:

    def __init__(self):
        pass

    def log_alert(self, message, level="INFO"):
        """Log an alert to the alerts log file."""
        if level == "CRITICAL":
            loguru.logger.critical(message)
            self._console_alert(message)
            self._email_alert(message)
        elif level == "ERROR":
            loguru.logger.error(message)
            self._console_alert(message)
        else:
            loguru.logger.info(message)

    def _console_alert(self, message):
        """Display an alert message on the console."""
        print(f"[ALERT] {message}")

    def _email_alert(self, message):
        """Send an email alert for critical issues."""
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'IDS Alert'
            msg['From'] = SMTP_USER
            msg['To'] = ALERT_EMAIL_RECIPIENT

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, [ALERT_EMAIL_RECIPIENT], msg.as_string())
            server.quit()
        except Exception as e:
            loguru.logger.error(f"Failed to send email alert: {e}")

# Sample Usage
if __name__ == "__main__":
    alert_handler = AlertHandler()
    alert_handler.log_alert("Suspicious HTTP signature detected: GET /admin", "CRITICAL")