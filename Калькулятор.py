# Вводимые значения: "ВВОД 5.0"; "СЛОЖИТЬ 2.0"; "УМНОЖИТЬ 3.0"; "ВЫВОД"

output_string = list()
number = 0.0

while True:
    input_string = input('Введите команду: ')
    if not input_string or input_string[0] == " ":
        print("Введена пустая строка, программа закончена.")
        break

    output_string = input_string.split()
    if output_string[0] == 'ВВОД':
        number = float(output_string[-1])
    elif output_string[0] == 'УМНОЖИТЬ':
        number = number * float(output_string[-1])
    elif output_string[0] == 'СЛОЖИТЬ':
        number = number + float(output_string[-1])
    elif output_string[0] == 'ВЫВОД':
        print('{:.3f}'.format(number))
