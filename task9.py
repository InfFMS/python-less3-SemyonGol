# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
N = int(input())
m = 100
M = 0
for i in range(1, N+1):
    a = int(input())
    if 100 > a > 9 and a%3 == 0:
        if a < m:
            m = a
        if a > M:
            M = a
if m == 100 and M == 0:
    print('None of input numbers are under conditions')
elif m == M:
    print('Only one number under conditions was inputed:', m)
else:
    print('Minimal number:',m, 'Maximal number:', M)
