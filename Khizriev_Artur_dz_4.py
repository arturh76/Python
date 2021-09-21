my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# инициализация переменных
message = ''

for item in my_list:
      message += item
      message += ' '
      result = message.split()[-1]
      print('Привет, ' + result.title() + '!')
