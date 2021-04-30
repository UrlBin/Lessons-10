number = int(input("Введите номер ячейки: "))
width = int(input("Введите ширину матрицу (width): "))

row = round(number / width - 1)
diference = width * (row + 1) - number
col = (width-1) - diference

print('Искомое значение строки (row) - ', row)
print('Искомое значение строки (col) - ', col)

