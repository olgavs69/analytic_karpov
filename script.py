import os

folders = [
    "python", "git", "sql", "теория вероятностей", "статистика", "визуализация",
    "развитие продукта", "продуктовая аналитика", "apache airflow", "проекты"
]

for folder in folders:
    try:
        os.makedirs(folder, exist_ok=True)
        print(f"Папка '{folder}' создана (или уже существует).")
    except Exception as e:
        print(f"Ошибка при создании папки '{folder}': {e}")
