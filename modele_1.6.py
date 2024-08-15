my_dict = {'David' : 2004, 'Dasha' : 2001, 'Dima' : 1976}
print(my_dict)
print(my_dict.get('David'))
print(my_dict.get('Denis', 'Такого ключа нет'))
my_dict.update({'Andrey' : 2003,
                'Ilya': 2000})
print(my_dict.get('Ilya'))
del my_dict['Ilya']
print(my_dict)


my_set = {1, 2, 3, 1, 2, "Name", True, (1, 2, 3, 4)}
print(my_set)
my_set.add(14.15)
my_set.add(12)
my_set.remove(1)
print(my_set)