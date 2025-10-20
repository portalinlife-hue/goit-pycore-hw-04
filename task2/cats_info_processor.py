def get_cats_info(path):
   
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = clean_line.split(',')
                # Перевіряємо, чи в рядку є рівно три частини: id, ім'я, вік
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_list.append(cat_dict)
                else:
                    print(f"Попередження: Некоректний формат рядка, рядок пропущено: '{clean_line}'")
        
        return cats_list

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        # Повертаємо порожній список у випадку помилки, як зазначено в завданні
        return []

# Шлях до файлу для другого завдання
cats_info = get_cats_info("task2/cats_data.txt")
print(cats_info)
