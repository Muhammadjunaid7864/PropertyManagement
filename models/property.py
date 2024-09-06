from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_paths = db.Column(db.Text)  # Store image paths as a comma-separated string
    location = db.Column(db.Text)
    property_type = db.Column(db.Text)
    status = db.Column(db.Text)
    beds = db.Column(db.Text)
    baths = db.Column(db.Text) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define the relationship to User
    owner = db.relationship('User', backref='properties', lazy=True)
