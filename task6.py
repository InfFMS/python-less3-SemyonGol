# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
a = 1
b = 1
m = 0
M = 0
while a != 0 or b != 0:
    a = int(input())
    b = int(input())
    if a >= b:
        M = a
        m = b
    else:
        m = a
        M = b
print(m, M)