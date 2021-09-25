# инициализация переменных
my_temp = ''
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in my_list:
    if i.isdigit() == True and int(i) < 10:
        print('"0{i}"'.format(i=i), end=" ")
        if i.isdigit() == True and int(i) > 10:
            print('{i}'.format(i=i), end=" ")
    else:
        print('"{i}"'.format(i=i), end=" ")


