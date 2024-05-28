n = int(input('Введите число от 3-х до 20-ти: '))
result = str()
a = int(n)
for i in range(1, n - 1):  # Вычисление пароля
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result = result + str(i) + str(j)
print(a, '-', result)













