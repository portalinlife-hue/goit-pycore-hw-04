import sys
import pathlib
from colorama import init, Fore

def display_directory_structure(directory_path, prefix=""):
    """
    Рекурсивно обходить директорію та виводить її структуру з кольорами.
    
    Args:
        directory_path (pathlib.Path): Об'єкт шляху до директорії.
        prefix (str): Префікс для візуального форматування дерева.
    """
    try:
        # Отримуємо вміст директорії.
        # Файли йдуть після папок для кращої візуалізації.
        items = sorted(list(directory_path.iterdir()), key=lambda x: x.is_file())
        
        # Створюємо "вказівники" для дерева
        pointers = ['┣━━ ' for _ in range(len(items) - 1)] + ['┗━━ ']

        for pointer, item in zip(pointers, items):
            if item.is_dir():
                # Виводимо директорію синім кольором
                print(f"{prefix}{pointer}{Fore.BLUE}{item.name}")
                # Рекурсивний виклик для піддиректорії
                extension = '┃   ' if pointer == '┣━━ ' else '    '
                display_directory_structure(item, prefix=prefix + extension)
            else:
                # Виводимо файл зеленим кольором
                print(f"{prefix}{pointer}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}Помилка доступу до директорії: {directory_path.name}")
    except Exception as e:
        print(f"{prefix}{Fore.RED}Не вдалося прочитати вміст: {directory_path.name}, помилка: {e}")

def main():
    """
    Головна функція для обробки аргументів та запуску візуалізації.
    """
    # Ініціалізуємо colorama для роботи в Windows
    init(autoreset=True)

    # Перевіряємо, чи був переданий аргумент командного рядка
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: Будь ласка, вкажіть шлях до директорії як аргумент.")
        print(Fore.YELLOW + "Приклад: python task-3/directory_visualizer.py .")
        return

    # Отримуємо шлях з аргументів
    directory_path = pathlib.Path(sys.argv[1])

    # Перевірки шляху
    if not directory_path.exists():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не існує.")
        return
    
    if not directory_path.is_dir():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не є директорією.")
        return

    print(Fore.CYAN + f"Структура директорії '{directory_path.resolve()}':")
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()
