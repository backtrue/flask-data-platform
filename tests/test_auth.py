"""
認證功能測試
"""
import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    """
    創建測試應用實例
    """
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """
    創建測試客戶端
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    創建測試 CLI 運行器
    """
    return app.test_cli_runner()

def test_login_page(client):
    """
    測試登入頁面訪問
    """
    response = client.get('/login')
    assert response.status_code == 200
    assert '登入'.encode('utf-8') in response.data

def test_login_success(client, app):
    """
    測試成功登入
    """
    with app.app_context():
        user = User(username='test', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        
        response = client.post('/login', data={
            'username': 'test',
            'password': 'password'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert '儀表板'.encode('utf-8') in response.data

def test_login_failure(client):
    """
    測試登入失敗
    """
    response = client.post('/login', data={
        'username': 'wrong',
        'password': 'wrong'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert '用戶名或密碼錯誤'.encode('utf-8') in response.data

def test_logout(client, app):
    """
    測試登出功能
    """
    with app.app_context():
        user = User(username='test', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        
        # 先登入
        client.post('/login', data={
            'username': 'test',
            'password': 'password'
        })
        
        # 測試登出
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200
        assert '登入'.encode('utf-8') in response.data 