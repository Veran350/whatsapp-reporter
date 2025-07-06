from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.services.email_service import EmailService
from app.services.validation import WhatsAppValidator
from app.services.recaptcha import verify_recaptcha
from app.models import Report, User
from app import db, limiter

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', 
                          recaptcha_site_key=current_app.config['RECAPTCHA_SITE_KEY'])

@main.route('/report', methods=['POST'])
@limiter.limit("5 per minute")
@login_required
def report_number():
    if not verify_recaptcha(request.form.get('recaptcha_response')):
        flash('reCAPTCHA verification failed', 'danger')
        return redirect(url_for('main.index'))
    
    whatsapp_number = request.form.get('number')
    is_valid, validation_msg = WhatsAppValidator.validate_number(whatsapp_number)
    
    if not is_valid:
        flash(validation_msg, 'danger')
        return redirect(url_for('main.index'))
    
    success, message, temp_email = EmailService.send_report(whatsapp_number)
    
    if success:
        report = Report(
            whatsapp_number=whatsapp_number,
            sender_email=temp_email,
            user_id=current_user.id
        )
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('main.success', number=whatsapp_number))
    
    flash(message, 'danger')
    return redirect(url_for('main.index'))

@main.route('/success')
def success():
    number = request.args.get('number', '')
    return render_template('success.html', number=number)