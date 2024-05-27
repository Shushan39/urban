def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()             # вывод  1 строка True
print_params(a=2, b=3)     # вывод  2 3 True
print_params(b=25)         # вывод  1 25 True
print_params(c=[1, 2, 3])  # вывод  1 строка [1, 2, 3]
values_list = [2, 2.5, 'SyntaxError']
values_dict = {'a': 'str', 'b': 2000, 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [55.55, 'Строка']
print_params(*values_list_2, 42)

