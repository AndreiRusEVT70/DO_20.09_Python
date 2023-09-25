import math
run = True
while run:
    a = float(input('Введите первое число = '))
    b = float(input('Введите второе число = '))

    op = int(input('Выберите операцию:\n'
                   '1 - вычитание,\n'
                   '2 - сложение,\n'
                   '3 - деление,\n'
                   '4 - умножение,\n'
                   '5 - возведения в квадрат,\n'
                   '6 - получение корня\n'))
    if op == 1:
        result = float(a - b)
        print(result)

    if op == 2:
        result = float(a + b)
        print(result)

    if op == 3:
        result = float(a / b)
        print(result)

    if op == 4:
        result = float(a * b)
        print(result)

    if op == 5:
        a2 = str(float(a**2))
        b2 = str(float(b**2))
        print(a2, b2)

    if op == 6:
       a3 = math.sqrt(a)
       b3 = math.sqrt(b)
       print(a3, b3)

    next = int(input('Выберите дальнейший шаг: \n1 - выход,\n2 - начать расчет заново\n'))

    if next == 1:
        run = False
