import random


bonus = random.choice([True, False])
salary = int(input("Enter salary: "))

if bonus:
    bonus_amount = random.randint(1, 100000)
    salary_result = salary + bonus_amount
else:
    bonus_amount = 0
    salary_result = salary

print(f"{salary}, {bonus} -'${salary_result}'")
