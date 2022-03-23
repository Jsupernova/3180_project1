import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_DATABASE_URI="postgres://cprwdznsnaetmt:b1370208c3c53a0fb35c51755e5a7d1d464d019dec9e5d13344fc4d4976f22c6@ec2-3-229-161-70.compute-1.amazonaws.com:5432/d30ifs1grvg7f2"
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = "./app/static/uploads"
