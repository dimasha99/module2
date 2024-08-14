def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result
from random import randint

number = 0
while number < 3 or number > 20:
    number = int(input("Введите число для пароля от 3 до 20: "))

password = generate_password(number)
print(f"Пароль для числа {number}: {password}")
print("Поздравляю,вы сбежали")
n= randint(3,20)
result = ""
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i + j) == 0 :
            result += f'{i}{j}'
print(f'{n} - {result}')