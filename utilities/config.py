import os

class Config:
    SECRET_KEY = 'your_secret_key'
    BASE_DIR = os.path.abspath(os.curdir)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'properties.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/img/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

    @staticmethod
    def ensure_instance_folder():
        instance_folder = os.path.join(Config.BASE_DIR, 'instance')
        if not os.path.exists(instance_folder):
            os.makedirs(instance_folder)
