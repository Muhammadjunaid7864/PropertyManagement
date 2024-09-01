from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_paths = db.Column(db.Text)  # Store image paths as a comma-separated string
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define the relationship to User
    owner = db.relationship('User', backref='properties', lazy=True)
