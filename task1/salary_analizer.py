def total_salary(path):
    try:
        total_sum = 0
        developer_count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                try:
                    parts = clean_line.split(',')
                    salary = int(parts[1])
                    
                    total_sum += salary
                    developer_count += 1
                
                except (ValueError, IndexError):
                    print(f"Попередження: Некоректний формат рядка, рядок пропущено: '{clean_line}'")

        if developer_count == 0:
            return 0, 0
            
        average_salary = total_sum / developer_count
        
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0, 0

total, average = total_salary("task1/salaries.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {int(average)}")

