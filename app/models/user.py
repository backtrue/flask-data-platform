"""
用戶模型模組
"""
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    """
    用戶模型類
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        """
        設置用戶密碼
        
        Args:
            password (str): 明文密碼
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        驗證用戶密碼
        
        Args:
            password (str): 待驗證的明文密碼
            
        Returns:
            bool: 密碼是否正確
        """
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    """
    用戶加載回調函數
    
    Args:
        id (int): 用戶 ID
        
    Returns:
        User: 用戶對象
    """
    return User.query.get(int(id)) 