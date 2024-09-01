from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from utilities.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)

# Ensure the instance folder exists
Config.ensure_instance_folder()

db.init_app(app)
login_manager.init_app(app)
from controllers import property 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    # Create tables and initial data
    from models.user import User

    db.create_all()

    # Check if the admin user exists and create if not
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', password='admin', needs_password_change=True)
        db.session.add(admin_user)
        db.session.commit()

from routes.app_routes import app_bp
app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(debug=True)
