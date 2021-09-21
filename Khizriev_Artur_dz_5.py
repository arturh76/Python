# инициализация переменных
result = ''
prices_decrease = []
prices_max = []
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63,
          39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11,
          18.34, 13, 64.80, 78, 93, 88.08]

# вывод значение с добавлением
for item in prices:
   if (type(item)) == int:
         print('%s руб 00 коп' % (item))
   else:
        item = str(item)
        r, kk = item.split('.')
        r = int(r)
        kk = int(kk)
        print('{r:} руб {kk:02d} коп'.format(r=r , kk=kk ))

# вывод списка отсортированного по сортированию
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
print()

# вывод списка отсортированного по убыванию
prices_decrease = sorted(prices, reverse=True)
print(prices_decrease)
print()

# вывод пяти максимальных цен, по возрастанию
prices_max = sorted(prices, reverse=True)
print(sorted(prices_max[0:5], reverse=False))

