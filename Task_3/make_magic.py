import re
from collections import Counter

def parse_log_line(line: str) -> dict:
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$"
    match = re.match(pattern, line)
    if match:
        date, cmd, log_info = match.groups()
        return {"date": date, "cmd": cmd, "log_info": log_info}
    return None

def load_logs(file_path: str):
    try:
        with open(file_path, "r", encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
    except FileNotFoundError:
        print(f"Файл за шляхом '{file_path}' не знайдено.")
        return None, None
    except IOError:
        print(f"Помилка читання файлу за шляхом '{file_path}'.")
        return None
    try:
        logs = [parse_log_line(el) for el in lines]
    except AttributeError:
        print("Помилка в обробці рядків файлу.")
        return None
    return logs    

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda el: el["cmd"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    return Counter(log['cmd'] for log in logs)

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for cmd, count in counts.items():
        print(f"{cmd:<16} | {count}")

