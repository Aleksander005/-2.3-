# "Нули ничто, отрицание недопустимо!

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0  # переменной индекса списка присваиваем 0
while len(my_list) > index:  # количество элементов списка больше индекса
    index = index + 1  # следующий индекс списка
    if my_list[index] > 0:  # если положительное
        print(my_list[index])  # печать
    if my_list[index] < 0:  # первое отрицательное
        break  # стоп

