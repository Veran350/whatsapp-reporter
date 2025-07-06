import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///reports.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # reCAPTCHA
    RECAPTCHA_SITE_KEY = os.getenv('RECAPTCHA_SITE_KEY')
    RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')
    
    # Email
    TARGET_EMAIL = os.getenv('TARGET_EMAIL')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = os.getenv('SMTP_PORT', 587)
    SMTP_USERNAME = os.getenv('SMTP_USERNAME')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    
    # Rate limiting
    RATE_LIMIT = os.getenv('RATE_LIMIT', '5 per minute')
    
    # Admin credentials
    ADMIN_USERNAME = 'Veran737'
    ADMIN_PASSWORD = '737veran777'