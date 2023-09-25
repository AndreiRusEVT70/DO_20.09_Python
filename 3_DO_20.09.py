a_string = input('Введите числа через пробел = ')
b = a_string.split(' ')
print(b)
c = list(map(float, b))

for d in c:
    if d == 5 or d ==7:
        c.remove(d)

print(c)

