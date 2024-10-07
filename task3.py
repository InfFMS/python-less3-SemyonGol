# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
a = int(input())
b = True
n = 0
p = 0
if a > 0:
    for i in range(2, a):
        if a%i == 0:
            b = False
    if not b:
        n += 1
    else:
        p += 1
else:
    n += 1
while a != 0:
    a = int(input())
    if a > 0:
        for i in range(2, a):
            if a%i == 0:
                b = False
        if not b:
            n += 1
        if b:
            p += 1
        b = True
    else:
        n += 1
print('Amount of prime numbers:', p, 'Amount of other integers:', n)