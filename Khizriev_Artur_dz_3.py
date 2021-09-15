percent = int(input('Введите число от 1 до 100: '))
if percent > 100:
    print("Вы введи число больше 100, повторить ввод")
    percent = int(input('Введите число от 1 до 100: '))
if percent % 10 == 1 and percent % 100 != 11:
    print(percent, 'процент,', end=" ")
elif 1 < percent % 10 < 5 and not 11 < percent % 100 < 1:
    print(percent, 'процента,', end=" ")
else:
    print(percent, 'процентов,', end=" ")