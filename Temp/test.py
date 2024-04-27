'''
from pathlib import Path


file_name = Path('./Temp')

def total_salary(path):
    total = 0
    count = 0
    file_path = path.resolve() / 'text.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            name, salary = line.strip().split(',')
            total += int(salary)
            count += 1
        if count > 0:
            average = total / count
        else:
            average = 0
    
        return total, average
    


total_salary(file_name)

total, average = total_salary(file_name)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
'''


from pathlib import Path
file_name = Path('./Temp')
def get_cats_info(path):
    cats_info = []
    file_path = Path(path).resolve() / 'text_cat.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) != 3:
                    continue
                
                cat_dict = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_dict)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка при читанні файлу:", e)
    
    return cats_info

cats_info = get_cats_info(file_name)
print(cats_info)
