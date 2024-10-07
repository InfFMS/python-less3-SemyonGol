# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
a = int(input())
deg2 = 0
n = 0
for i in range(1, 1024):
    if a == 2**i:
        deg2 += a
        n += 1
if a ==0:
    n += 1
while a != 0:
    a = int(input())
    for i in range(1, 1024):
        if a == 2**i:
            deg2 += a
            n += 1
print('Arithmetic mean of numbers in format 2**n:', deg2/n)