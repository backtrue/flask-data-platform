"""
應用配置文件
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """
    應用配置類
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Google Analytics 配置
    GOOGLE_ANALYTICS_CREDENTIALS = os.environ.get('GOOGLE_ANALYTICS_CREDENTIALS')
    GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID') 