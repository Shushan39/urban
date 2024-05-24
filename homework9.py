n = int(input('Введите число от 3 до 20'))
for i in range(1, n - 1):
    for j in range(i + 1, n):
        c = i + j
        if n % c == 0:
            print(i, j)













