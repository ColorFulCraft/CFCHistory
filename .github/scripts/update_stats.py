import json
import os
from datetime import datetime, timezone, timedelta
import requests

def update_stats():
    # 文件路径
    stats_file = 'stats/visit_stats.json'
    
    # 确保stats目录存在
    os.makedirs('stats', exist_ok=True)
    
    # 获取当前日期（UTC+8）
    beijing_tz = timezone(timedelta(hours=8))
    current_date = datetime.now(beijing_tz).strftime('%Y-%m-%d')
    current_hour = datetime.now(beijing_tz).strftime('%Y-%m-%d %H:00:00')
    
    # 读取现有统计数据
    if os.path.exists(stats_file):
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
    else:
        stats = {
            "total_visits": 0,
            "daily_visits": {},
            "hourly_visits": {},
            "last_updated": "",
            "last_updated_date": current_date
        }
    
    # 检查是否需要重置今日访问量（新的一天）
    last_updated_date = stats.get('last_updated_date', '')
    if last_updated_date != current_date:
        # 新的一天，重置今日访问量但保留累计访问量
        stats['daily_visits'] = {}
        stats['hourly_visits'] = {}
        stats['last_updated_date'] = current_date
    
    # 估算实时访问量（基于工作流运行间隔）
    # 假设每次工作流运行代表有新的访问
    estimated_increment = 3  # 可以根据实际情况调整
    
    # 更新统计数据
    stats['total_visits'] += estimated_increment
    
    # 更新今日访问量（当前小时）
    stats['hourly_visits'][current_hour] = stats['hourly_visits'].get(current_hour, 0) + estimated_increment
    
    # 计算今日总访问量（所有小时之和）
    today_total = sum(stats['hourly_visits'].values())
    stats['daily_visits'][current_date] = today_total
    
    stats['last_updated'] = datetime.now(beijing_tz).isoformat()
    
    # 保存更新后的数据
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"Statistics updated: Total={stats['total_visits']}, Today={today_total}")

if __name__ == '__main__':
    update_stats()
