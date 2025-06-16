# 貢獻指南

感謝您對 Flask 數據平台感興趣！我們歡迎各種形式的貢獻，包括但不限於：

- 報告問題
- 提交功能建議
- 改進文檔
- 提交代碼修改

## 如何貢獻

1. Fork 本專案
2. 創建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

## 開發環境設置

1. 克隆專案
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

4. 設置環境變量
```bash
cp .env.example .env
# 編輯 .env 文件設置必要的配置
```

5. 初始化數據庫
```bash
python init_db.py
```

## 代碼風格

- 遵循 PEP 8 風格指南
- 使用有意義的變量名和函數名
- 添加適當的註釋和文檔字符串
- 確保所有測試通過

## 提交規範

提交信息應該清晰描述更改的內容，建議使用以下格式：

```
類型: 簡短描述

詳細描述（如果需要）
```

類型包括：
- feat: 新功能
- fix: 修復問題
- docs: 文檔更改
- style: 代碼格式（不影響代碼運行的變動）
- refactor: 重構（既不是新增功能，也不是修改 bug 的代碼變動）
- test: 增加測試
- chore: 構建過程或輔助工具的變動

## 問題反饋

如果您發現任何問題或有改進建議，請在 GitHub Issues 中提交。提交問題時，請包含：

- 問題的詳細描述
- 重現步驟
- 預期行為
- 實際行為
- 環境信息（操作系統、Python 版本等）

## 行為準則

- 尊重所有社區成員
- 接受建設性的批評
- 關注問題本身
- 保持專業和友善的交流氛圍

感謝您的貢獻！ 