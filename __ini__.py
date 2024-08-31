from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utilities.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure the instance folder exists
    Config.ensure_instance_folder()

    db.init_app(app)

    with app.app_context():
        # Create tables and initial data
        from models import User
        db.create_all()

        # Check if the admin user exists and create if not
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin', password='admin', needs_password_change=True)
            db.session.add(admin_user)
            db.session.commit()

    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
