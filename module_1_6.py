# Работа со словарями
my_dict = {'Имя' :'Антон', 'Год рождения' : 1990, 'Месяц рождения' : 'Август', 'Возраст' :34}
print('Dict:' + str(my_dict))

print('Existing value:' + str(my_dict['Год рождения']))
print('Not existing value:' + str(my_dict.get('Хобби')))

my_dict.update({'Хобби' : 'Туризм', 'Телефон' : 89912345433})

a = my_dict.pop('Имя')
print('Deleted value:' + str(a))

print('Modifield dictionary:' + str(my_dict))


# Работа с множествами
my_set = {'a', 'b', 'c', 'd', 'a', 'c', 'b', 'd', 3, 5, True}
print('Set:' + str(set(my_set)))

my_set.update({'e', 8})
my_set.discard('d')
print('Modified set: ' + str(my_set))
































