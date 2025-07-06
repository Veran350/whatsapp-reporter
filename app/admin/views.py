from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Report, User

admin = Blueprint('admin', __name__)

@admin.before_request
@login_required
def require_admin():
    if not current_user.is_admin:
        return redirect(url_for('main.index'))

@admin.route('/')
def dashboard():
    reports = Report.query.order_by(Report.date_reported.desc()).all()
    users = User.query.all()
    return render_template('admin/reports.html', reports=reports, users=users)