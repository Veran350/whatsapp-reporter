import smtplib
import random
from datetime import datetime
from config import Config

class EmailService:
    @staticmethod
    def generate_temp_email():
        domains = ["1secmail.com", "1secmail.net", "1secmail.org"]
        domain = random.choice(domains)
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
        return f"{name}@{domain}"

    @staticmethod
    def send_report(whatsapp_number):
        temp_email = EmailService.generate_temp_email()
        subject = f"WhatsApp Number Report: {whatsapp_number}"
        body = f"""New WhatsApp number report:

Number: {whatsapp_number}
Reported at: {datetime.now()}
Sender Temp Email: {temp_email}

This is an automated report from the WhatsApp reporting system.
"""
        
        try:
            with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
                server.starttls()
                if Config.SMTP_USERNAME and Config.SMTP_PASSWORD:
                    server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
                server.sendmail(temp_email, Config.TARGET_EMAIL, f"Subject: {subject}\n\n{body}")
            return True, "Report submitted successfully", temp_email
        except Exception as e:
            return False, f"Failed to send report: {str(e)}", None