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