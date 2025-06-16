"""
認證控制器模組
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    用戶登入處理
    
    Returns:
        Response: 重定向到儀表板或登入頁面
    """
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard.index'))
            
        flash('用戶名或密碼錯誤', 'error')
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """
    用戶登出處理
    
    Returns:
        Response: 重定向到登入頁面
    """
    logout_user()
    return redirect(url_for('auth.login')) 