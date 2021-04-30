row = int(input("Введите номер строки (row): "))
col = int(input("Введите номер столбца (col): "))
width = int(input("Введите ширину матрицу (width): "))

answer = width * (row + 1) - (width - col - 1)
print('Искомое значение - ', answer)

