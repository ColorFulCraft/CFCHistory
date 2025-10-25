import json
import os
from datetime import datetime, timezone, timedelta

def update_stats():
    # 文件路径
    stats_file = 'stats/visit_stats.json'
    
    # 确保stats目录存在
    os.makedirs('stats', exist_ok=True)
    
    # 读取现有统计数据
    if os.path.exists(stats_file):
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
    else:
        stats = {
            "total_visits": 0,
            "daily_visits": {},
            "last_updated": ""
        }
    
    # 获取当前日期（UTC+8）
    beijing_tz = timezone(timedelta(hours=8))
    current_date = datetime.now(beijing_tz).strftime('%Y-%m-%d')
    
    # 更新统计数据
    stats['total_visits'] += 1
    stats['daily_visits'][current_date] = stats['daily_visits'].get(current_date, 0) + 1
    stats['last_updated'] = datetime.now(beijing_tz).isoformat()
    
    # 保存更新后的数据
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"Statistics updated: Total {stats['total_visits']}, Today {stats['daily_visits'][current_date]}")

if __name__ == '__main__':
    update_stats()
