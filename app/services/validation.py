import re

class WhatsAppValidator:
    @staticmethod
    def validate_number(number):
        if not number:
            return False, "Number cannot be empty"
        
        pattern = r'^\+\d{8,15}$'
        if not re.match(pattern, number):
            return False, "Invalid format. Use international format (+[country code][number])"
        
        return True, "Valid number"