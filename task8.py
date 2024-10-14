# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).
N = int(input())
p = 0
n = 0
for i in range(1, N+1):
    a = int(input())
    if a < 0:
        n += 1
    elif a > 0:
        p += 1
print('Negative numbers:', n, 'Positive numbers:' ,p)