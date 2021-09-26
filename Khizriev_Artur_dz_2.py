# инициализация переменных
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in my_list:
    i = i.replace("+", "").replace("-", '')
    if i.isdigit() == True and int(i) < 10:
        print('"0{i}"'.format(i=i), end=" ")
        if i.isdigit() == True and int(i) > 10:
            print('{i}'.format(i=i), end=" ")
    else:
            print('"{i}"'.format(i=i), end=" ")