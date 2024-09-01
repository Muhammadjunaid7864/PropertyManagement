from app import db

class User(db.Model):
    try:
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(120), nullable=False)
        needs_password_change = db.Column(db.Boolean, default=False)
        


        def __repr__(self):
            return f'<User {self.username}>'
        
        def is_active(self):
            # Return True if the user is active
            return True

        def is_authenticated(self):
            # Return True if the user is authenticated
            return True

        def is_anonymous(self):
            # Return False if the user is not anonymous
            return False

        def get_id(self):
            # Return the user id
            return str(self.id)
    except Exception as error:
        print(error)

