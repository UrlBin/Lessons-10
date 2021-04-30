# Заданные уравнения
# y = x
# x**2 - 4*x + 3

my_list = list()
output_dictionary = dict([])
out_list = list()

N = int(input('Введите натуральное число количества точек: '))
for i in range(0, N):
    x_coordinate_of_point = float(input('Введите значение, это будет координата "x" очередной точки: '))
    y_coordinate_of_point = float(input('Введите значение, это будет координата "y" очередной точки: '))
    my_list.append(list((x_coordinate_of_point, y_coordinate_of_point)))

for j in my_list:
    if j[0] > (j[0]**2 - 4*j[0] + 3) and j[1] < j[0] and j[1] < j[0]:
        output_dictionary[j[0]] = j[1]

if len(output_dictionary) == 0:
    print('Ни одна точка не попала в заданное поле.')
else:
    for k in output_dictionary.items():
        print('(', int(k[0]), ', ', int(k[1]), ')', sep='')

