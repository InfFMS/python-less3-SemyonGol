# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
e = 0
d = 0
a = int(input())
if a > 0 and a < 100:
    d += 1
else:
    e += 1
while a != 0:
    a = int(input())
    if a > 0 and a < 100:
        d += 1
    else:
        e += 1
print('Number of two-digit integers > 0:', d, 'Number of other integers:', e)