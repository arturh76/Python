# инициализация переменных
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in my_list:
    sign = i[0] if i[0] in "+-" else ""
    i = i.replace("+", "").replace("-", "")
    if i.isdigit() and int(i) < 10:
        print('"{}0{}"'.format(sign, i), end=" ")
    elif i.isdigit() and int(i) > 10:
        print('"{}{}"'.format(sign, i), end=" ")
    else:
        print('"{}"'.format(i), end=" ")

