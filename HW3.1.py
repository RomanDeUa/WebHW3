import os
import shutil
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

# Функція для копіювання файлу в цільову директорію
def copy_file(file_path, target_dir):
    ext = os.path.splitext(file_path)[1][1:].lower()  # Отримуємо розширення файлу без точки
    if not ext:
        return  # Пропускаємо файли без розширення
    ext_dir = os.path.join(target_dir, ext)  # Директорія для відповідного розширення
    os.makedirs(ext_dir, exist_ok=True)  # Створюємо директорію, якщо вона не існує
    shutil.copy(file_path, ext_dir)  # Копіюємо файл

# Функція для обробки директорій
def process_directory(source_dir, target_dir):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(copy_file, file_path, target_dir)

# Головна функція
def main():
    # Отримуємо шляхи до джерела і цілі
    if len(sys.argv) < 2:
        print("Використання: python HW3.1.py <source_dir> [<target_dir>]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"
    
    if not os.path.exists(source_dir):
        print(f"Джерельна директорія {source_dir} не існує.")
        sys.exit(1)
    
    os.makedirs(target_dir, exist_ok=True)
    
    # Запуск багатопотокової обробки
    process_directory(source_dir, target_dir)
    print(f"Файли успішно скопійовані та відсортовані до {target_dir}.")

if __name__ == "__main__":
    main()


# Використання:   python HW3.1 <шлях до директорії з файлами> <шлях до цільової директорії куди складати>
