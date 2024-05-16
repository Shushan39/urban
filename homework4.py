immutable_var = 1, 2, True, 'apple'
print(immutable_var)
#immutable_var[-1] = 'pear' кортеж не поддерживает обращение к элементам
mutable_list = ['bmv', 'audi', 'toyota']
print(mutable_list)
mutable_list[2] = 'mercedes'
print(mutable_list)
mutable_list.reverse()
print(mutable_list)
mutable_list.insert(0, 'toyota')
print(mutable_list)