"""
管理員控制器模組
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.user import User
from app import db
from functools import wraps

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    """
    管理員權限裝飾器
    
    Args:
        f: 被裝飾的函數
        
    Returns:
        function: 裝飾後的函數
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('需要管理員權限', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    """
    管理員儀表板
    
    Returns:
        Response: 管理員儀表板頁面
    """
    return render_template('admin/dashboard.html')

@admin_bp.route('/users')
@login_required
@admin_required
def users():
    """
    用戶管理頁面
    
    Returns:
        Response: 用戶列表頁面
    """
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin_bp.route('/users/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    """
    創建用戶
    
    Returns:
        Response: 創建用戶頁面或重定向到用戶列表
    """
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        is_admin = request.form.get('is_admin') == 'on'
        
        if User.query.filter_by(username=username).first():
            flash('用戶名已存在', 'error')
            return redirect(url_for('admin.create_user'))
            
        user = User(username=username, email=email, is_admin=is_admin)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('用戶創建成功', 'success')
        return redirect(url_for('admin.users'))
        
    return render_template('admin/create_user.html')

@admin_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    """
    編輯用戶
    
    Args:
        user_id (int): 用戶 ID
        
    Returns:
        Response: 編輯用戶頁面或重定向到用戶列表
    """
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.is_admin = request.form.get('is_admin') == 'on'
        
        if request.form.get('password'):
            user.set_password(request.form.get('password'))
            
        db.session.commit()
        flash('用戶更新成功', 'success')
        return redirect(url_for('admin.users'))
        
    return render_template('admin/edit_user.html', user=user)

@admin_bp.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    """
    刪除用戶
    
    Args:
        user_id (int): 用戶 ID
        
    Returns:
        Response: 重定向到用戶列表
    """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('用戶刪除成功', 'success')
    return redirect(url_for('admin.users')) 