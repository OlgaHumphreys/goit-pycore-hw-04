import os


def total_salary(path):
    salary_amount = 0
    if not os.path.exists(path):
        return 0, 0

    with open(path,"r",encoding="UTF-8") as file:
        lines = file.readlines()

        if len(lines) == 0:
            return 0,0


        for line in lines:
            try: 
                salary = line.split(",")[1].replace("/n","")
                salary_amount += int(salary)

            except (IndexError, ValueError): 
                return 0,0
        salary_average = int(salary_amount/len(lines))
    return salary_amount, salary_average


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

