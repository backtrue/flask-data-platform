# Flask 數據平台

一個基於 Flask 的數據分析平台，提供用戶管理、數據可視化和 Google Analytics 整合等功能。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.0%2B-blue.svg)](https://flask.palletsprojects.com/)

## 功能特點

- 用戶認證和授權
- 管理員控制面板
- 數據可視化儀表板
- Google Analytics 整合
- 響應式設計

## 技術棧

- 後端：Flask + SQLAlchemy
- 前端：Bootstrap 5 + Vue.js 3
- 數據庫：SQLite
- 圖表庫：Chart.js
- 認證：Flask-Login

## 安裝說明

1. 克隆倉庫
```bash
git clone https://github.com/backtrue/flask-data-platform.git
cd flask-data-platform
```

2. 創建虛擬環境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安裝依賴
```bash
pip install -r requirements.txt
```

4. 配置環境變量
```bash
cp .env.example .env
# 編輯 .env 文件設置必要的配置
```

5. 初始化數據庫
```bash
python init_db.py
```

6. 運行應用
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
│   ├── templates/     # 模板文件
│   └── __init__.py    # 應用初始化
├── tests/             # 測試文件
├── config.py          # 配置文件
├── init_db.py         # 數據庫初始化
└── run.py            # 應用入口
```

### 添加新功能
1. 在 `app/models/` 中創建數據模型
2. 在 `app/controllers/` 中實現業務邏輯
3. 在 `app/templates/` 中創建視圖模板
4. 在 `tests/` 中添加測試用例

### 運行測試
```bash
pytest
```

## 部署說明

1. 設置生產環境變量
2. 配置數據庫連接
3. 設置 Google Analytics 憑證
4. 使用生產級 WSGI 服務器（如 Gunicorn）

## 貢獻指南

請查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何為本項目做出貢獻。

## 授權

本項目採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 文件

## 作者

- backtrue - [GitHub](https://github.com/backtrue)

## 致謝

- Flask 團隊
- Bootstrap 團隊
- Vue.js 團隊
- Chart.js 團隊 