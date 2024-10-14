# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".

N = int(input())
m = 2**100
M = 0
b = True
for i in range(1, N+1):
    a = int(input())
    for o in range(2, a):
        if a%o == 0:
            b = False
    if b:
        if a > M:
            M = a
        if a < m:
            m = a
    b = True
if M == 0 and m == 2**100:
    print('None of input numbers are prime')
elif m == 2**100 or M == 0 or m == M:
    print('Only one prime was inputed:',M)
else:
    print('Minimal prime:', m,'Maximal prime:', M)