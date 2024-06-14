import random
n_case = random.randint(3,20)
print("Случайное число:", n_case)
numbers = ""
for i in range(1, n_case):
    for j in range (i, n_case):
        if n_case % (i + j) == 0 and i !=j:
            numbers = numbers + f"{i}" + f"{j}"
print(numbers)

