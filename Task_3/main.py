from pathlib import Path
import sys
import make_magic


def main():
    if len(sys.argv) < 2:
        print("Введить шлях до файлу в консоль:")
        return
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: The file '{file_path}' does not exist.")
        return
    
    parsed_logs = make_magic.load_logs(file_path)
    count_logs = make_magic.count_logs_by_level(parsed_logs)
    make_magic.display_log_counts(count_logs)
    
    if len(sys.argv) > 2:
        log_level = sys.argv[2]
        log_details = make_magic.filter_logs_by_level(parsed_logs, log_level)
        print(f"Деталі логів для рівня '{log_level}':")
        for detail in log_details:
            print(f"{detail['date']} - {detail['log_info']}")

if __name__ == "__main__":
   main()