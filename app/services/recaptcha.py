import requests
from flask import current_app

def verify_recaptcha(response):
    if not current_app.config['RECAPTCHA_SECRET_KEY']:
        return True
    
    data = {
        'secret': current_app.config['RECAPTCHA_SECRET_KEY'],
        'response': response
    }
    result = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data=data
    ).json()
    
    return result.get('success', False)