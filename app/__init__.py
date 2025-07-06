from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    limiter.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from app.routes import main
    from app.auth.routes import auth
    from app.admin.views import admin

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)

    with app.app_context():
        db.create_all()
        # Create admin user if not exists
        from app.models import User
        admin_user = User.query.filter_by(username=app.config['ADMIN_USERNAME']).first()
        if not admin_user:
            admin_user = User(
                username=app.config['ADMIN_USERNAME'],
                email='admin@example.com',
                password=app.config['ADMIN_PASSWORD'],
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()

    return app