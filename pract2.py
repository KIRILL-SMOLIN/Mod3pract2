  # Самостоятельная работа по уроку "Распаковка параметров и параметры функции"
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(5)
print_params(7, 9)
print_params(b = 25)    # Работает
print_params(c = [1,2,3])   # Работает

values_list = [1, 'один', True]
values_dict = {'a': 2, 'b': 'линия', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 15.18]
print_params(*values_list_2, 42)  # Работает
