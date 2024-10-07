my_dict = {'Ivan' : 1990, 'Andrew' :1992,}
print(my_dict)
print(my_dict['Andrew'])
print(my_dict.get('Denis', 'отсутсвует искомый парень'))
my_dict.update({'Denis' : 1991,
                'Max' : 1989})
print(my_dict)
del my_dict['Denis']
print(my_dict.get('Denis', 'Max'))
print(my_dict)
#
my_set = {1, 2, 3, 4, 5, 3, 2, 'world', ('apple', 'mango', 'tomato')}
print(my_set)
my_set.update({'trouble', 6, 7, 8, 9,5,6,4})
print(my_set)
print(my_set.remove('trouble'))
print(my_set)
