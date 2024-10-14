# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
a = int(input())
sum5 = 0
if a%5 == 0:
    sum5 += a
while a != 0:
    a = int(input())
    if a%5 == 0:
        sum5 += a
print('Sum of integers that divisible by 5:', sum5)