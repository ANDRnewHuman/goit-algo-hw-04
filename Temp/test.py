
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






