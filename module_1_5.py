immutable_var = 10, 15, 'string', True
print('immutable_var:' + str(immutable_var))

#immutable_var[1] = 20
#print(immutable_var)   Программа выдает ошибку: "В объекте  tuple нельзя изменить значение элемента, ну или как то так)

mutable_list = [[1,2], 10, 15, 'string', True]
mutable_list[0][0]= 30
mutable_list[2] = 40
mutable_list[4]= False
print('mutable_list:' + str(mutable_list)) # Изменены 3 элемента в списке


