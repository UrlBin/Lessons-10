# Input lines with tabs:
# 0    1    2
# 3    4    5
# 6    7    8
# или
# 1    2
# 3    4

output_matrix = list()
matrix_line = list()
matrix = list()

# Ввод строк для обработки. Вводим количество строк, зависящее от количества введеных элементов первой строки.
matrix.append(input().split('\t'))
for i in range(1, len(matrix[0])):
    matrix.append(input().split('\t'))
print(matrix)
# Транспонирование.
for j in range(0, len(matrix[0])):
    for k in range(0, len(matrix[0])):
        matrix_line.append(matrix[k][j])
        print('1 ', matrix_line)
        print('2 ', output_matrix)
    output_matrix.append(matrix_line)
    print('output_matrix', output_matrix)
    matrix_line.clear()

print(output_matrix)