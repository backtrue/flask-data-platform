"""
數據庫初始化腳本
"""
from app import create_app, db
from app.models.user import User

def init_db():
    """
    初始化數據庫並創建管理員用戶
    """
    app = create_app()
    with app.app_context():
        # 創建所有表
        db.create_all()
        
        # 檢查是否已存在管理員用戶
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@example.com',
                is_admin=True
            )
            admin.set_password('admin123')  # 請在生產環境中更改此密碼
            db.session.add(admin)
            db.session.commit()
            print('管理員用戶創建成功！')
        else:
            print('管理員用戶已存在。')

if __name__ == '__main__':
    init_db() 