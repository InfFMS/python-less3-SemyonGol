#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
a = int(input())
p=0
n=0
if a > 0:
    p += 1
if a < 0:
    n += 1
while a != 0:
    a = int(input())
    if a > 0:
        p +=1
    if a < 0:
        n +=1
print('Number of positive integers:', p, '; number of negative integers:', n)