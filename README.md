# 數據平台

這是一個基於 Flask 的數據分析平台，提供用戶管理、數據可視化和 Google Analytics 整合功能。

## 功能特點

- 用戶認證系統
- 管理員控制面板
- 數據可視化儀表板
- Google Analytics 整合
- 響應式設計

## 技術棧

- 後端：Flask + SQLAlchemy
- 前端：Bootstrap 5 + Vue.js 3
- 數據庫：SQLite（可配置為其他數據庫）
- 圖表：Chart.js
- 認證：Flask-Login

## 安裝步驟

1. 克隆代碼庫：
```bash
git clone <repository-url>
cd flask_dataplatform
```

2. 創建並激活虛擬環境：
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 安裝依賴：
```bash
pip install -r requirements.txt
```

4. 配置環境變量：
```bash
cp .env.example .env
# 編輯 .env 文件，設置必要的配置項
```

5. 初始化數據庫：
```bash
python init_db.py
```

6. 運行應用：
```bash
python run.py
```

## 開發指南

### 目錄結構

```
flask_dataplatform/
├── app/
│   ├── controllers/    # 控制器
│   ├── models/        # 數據模型
│   ├── static/        # 靜態文件
│   └── templates/     # 模板文件
├── tests/             # 測試文件
├── .env              # 環境變量
├── config.py         # 配置文件
├── requirements.txt  # 依賴列表
└── run.py           # 應用入口
```

### 添加新功能

1. 在 `app/models/` 中創建新的數據模型
2. 在 `app/controllers/` 中創建新的控制器
3. 在 `app/templates/` 中添加新的模板
4. 在 `app/static/` 中添加新的靜態文件

### 運行測試

```bash
pytest
```

## 部署

1. 設置生產環境變量
2. 配置數據庫連接
3. 設置 Google Analytics 憑證
4. 使用生產級 WSGI 服務器（如 Gunicorn）

## 貢獻指南

1. Fork 項目
2. 創建功能分支
3. 提交更改
4. 發起 Pull Request

## 授權

MIT License 