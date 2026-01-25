import json
import os
from datetime import datetime, timezone, timedelta
from collections import OrderedDict

def update_stats():
    # 文件路径
    stats_file = 'stats/visit_stats.json'
    
    # 确保stats目录存在
    os.makedirs('stats', exist_ok=True)
    
    # 获取当前日期（UTC+8）
    beijing_tz = timezone(timedelta(hours=8))
    now = datetime.now(beijing_tz)
    current_date = now.strftime('%Y-%m-%d')
    current_hour = now.strftime('%Y-%m-%d %H:00:00')
    
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
    
    # 清理旧数据（保留最近7天的数据）
    cleanup_old_data(stats, now)
    
    stats['last_updated'] = now.isoformat()
    
    # 保存更新后的数据
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"Statistics updated: Total={stats['total_visits']}, Today={today_total}")

def cleanup_old_data(stats, current_time):
    """清理旧数据，只保留最近7天的数据"""
    beijing_tz = timezone(timedelta(hours=8))
    
    # 清理hourly_visits：只保留最近7天
    cutoff_date = current_time - timedelta(days=7)
    cutoff_str = cutoff_date.strftime('%Y-%m-%d')
    
    # 创建新的hourly_visits字典，只保留最近7天的数据
    new_hourly = {}
    for hour_str, count in stats['hourly_visits'].items():
        hour_date = hour_str.split(' ')[0]  # 获取日期部分
        if hour_date >= cutoff_str:
            new_hourly[hour_str] = count
    
    stats['hourly_visits'] = dict(OrderedDict(sorted(new_hourly.items())))
    
    # 清理daily_visits：只保留最近7天
    new_daily = {}
    for date_str, count in stats['daily_visits'].items():
        if date_str >= cutoff_str:
            new_daily[date_str] = count
    
    stats['daily_visits'] = dict(OrderedDict(sorted(new_daily.items())))
    
    print(f"Cleaned up data older than {cutoff_str}")

if __name__ == '__main__':
    update_stats()
