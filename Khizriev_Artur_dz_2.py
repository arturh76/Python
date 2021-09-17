cube_list = []
my_list = []
n_sum = 0
all_sum = 0
idx = 0

# инициализируем переменные
list_of_cubes = []
add_list_of_cubes = []
all_sum = 0

# заполняем список значениями в дапазоне от 1 до 1000
# с шагом 2 - нечетные значения
# 1 + 2 = 3
# 3 + 2 = 5
# и т.д.

# каждый элемент возводим в куб при добавлении в список
for i in range(1, 1000, 2):
    list_of_cubes.append(i ** 3)

# перебираем элементы списка
for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10  # "отрезаем" последнюю цифру
        val //= 10  # удаляем последнюю цифру
    if sum_digits % 7 == 0:  # фильтр на кратность 7
        all_sum += list_of_cubes[ind]

print(all_sum)

for m in list_of_cubes:
    add_list_of_cubes.append(m + 17)

# обнуляем значеие переменной для возможности её повторного использования
all_sum = 0

for ind, val in enumerate(add_list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10  # "отрезаем" последнюю цифру
        val //= 10  # удаляем последнюю цифру
    if sum_digits % 7 == 0:  # фильтр на кратность 7
        all_sum += add_list_of_cubes[ind]

print(all_sum)

# 17485588610
# 15392909930



