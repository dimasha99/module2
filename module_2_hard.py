while True:
    number = int(input('Введите число от 3 до 20: '))
    result = ''

    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i+j) == 0:
                result += f'{i}{j}'
    print(f'{number} - {result}')
