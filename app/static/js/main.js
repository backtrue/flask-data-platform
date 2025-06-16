/**
 * 全局工具函數
 */
const utils = {
    /**
     * 格式化日期
     * @param {string|Date} date - 日期對象或日期字符串
     * @param {string} format - 格式化模板
     * @returns {string} 格式化後的日期字符串
     */
    formatDate(date, format = 'YYYY-MM-DD HH:mm:ss') {
        const d = new Date(date);
        const year = d.getFullYear();
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const day = String(d.getDate()).padStart(2, '0');
        const hours = String(d.getHours()).padStart(2, '0');
        const minutes = String(d.getMinutes()).padStart(2, '0');
        const seconds = String(d.getSeconds()).padStart(2, '0');

        return format
            .replace('YYYY', year)
            .replace('MM', month)
            .replace('DD', day)
            .replace('HH', hours)
            .replace('mm', minutes)
            .replace('ss', seconds);
    },

    /**
     * 格式化數字
     * @param {number} num - 要格式化的數字
     * @param {number} decimals - 小數位數
     * @returns {string} 格式化後的數字字符串
     */
    formatNumber(num, decimals = 0) {
        return num.toLocaleString('zh-TW', {
            minimumFractionDigits: decimals,
            maximumFractionDigits: decimals
        });
    },

    /**
     * 顯示通知
     * @param {string} message - 通知消息
     * @param {string} type - 通知類型（success/error/warning/info）
     */
    showNotification(message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        document.querySelector('main').insertBefore(alertDiv, document.querySelector('main').firstChild);
        
        // 5秒後自動關閉
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
};

/**
 * 頁面加載完成後執行
 */
document.addEventListener('DOMContentLoaded', () => {
    // 初始化所有工具提示
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // 初始化所有彈出框
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // 自動關閉警告框
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}); 