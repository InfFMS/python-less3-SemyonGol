# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
a = int(input())
m = a
M = a
while a != 0:
    a = int(input())
    if a==0:
        break
    elif a > M:
        M = a
    elif a < m:
        m = a
print('Minimum number:',m,'Maximum number:', M)