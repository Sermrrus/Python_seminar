names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
print({names[i]: float(salary[i] * int(bonus[i].strip("%")) / 100) for i in range(len(names))})
