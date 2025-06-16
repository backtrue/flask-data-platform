"""
Flask 應用初始化模組
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
from config import Config

# 初始化擴展
db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name='數據平台管理', template_mode='bootstrap4')
migrate = Migrate()

def create_app(config_class=Config):
    """
    創建並配置 Flask 應用
    
    Args:
        config_class: 配置類
        
    Returns:
        Flask: 配置好的 Flask 應用實例
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化擴展
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)

    # 註冊藍圖
    from app.controllers.auth import auth_bp
    from app.controllers.dashboard import dashboard_bp
    from app.controllers.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)

    return app 