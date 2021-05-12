# Выражение для ввода - 1+2*3*4+5      1 + 2 *  3 * 4  + 5.0
string_for_calculation = ''

input_string = input('Введите строку для парсинга арифметических выражений: ')

storage_numerics = []
storage_sign = []

number = ''
for i in range(0, len(input_string)):
    if input_string[i].isdigit() or input_string[i] == '.':
        number += input_string[i]
        if i == len(input_string) - 1:
            storage_numerics.append(number)
            # print('storage_numerics', storage_numerics)
            break
        # print('number', number)
    elif input_string[i] == ' ' and not storage_numerics:
        continue
    elif input_string[i] == ' ' and storage_numerics and number != '':
        storage_numerics.append(number)
        # print('storage_numerics', storage_numerics)
        number = ''
    else:
        if input_string[i] == '*' or input_string[i] == '+':
            storage_sign.append(input_string[i])
        # print('storage_sign', storage_sign)
        if number != '':
            storage_numerics.append(number)
            # print('storage_numerics', storage_numerics)
        number = ''

print('storage_numerics', storage_numerics)
print('storage_sign', storage_sign)

for j in range(0, len(storage_sign) - 1):
    if storage_sign[j] == '+' and j != len(storage_sign) - 2:
        storage_numerics.append(storage_numerics.pop(j))
        storage_sign.append(storage_sign.pop(j))

print('storage_numerics', storage_numerics)
print('storage_sign', storage_sign)

for j in range(0, len(storage_sign)):
    if storage_sign[j] == '*' and j == 0:
        if storage_numerics[j].isdecimal() or storage_numerics[j + 1].isdecimal():
            string_for_calculation = int(storage_numerics[j]) * int(storage_numerics[j + 1])
            print('string_for_calculation in "*" -> ', string_for_calculation)
        else:
            string_for_calculation = float(storage_numerics[j]) * float(storage_numerics[j + 1])
            print('string_for_calculation in "*" -> ', string_for_calculation)
    elif storage_sign[j] == '*':
        if storage_numerics[j].isdecimal():
            string_for_calculation *= int(storage_numerics[j + 1])
        else:
            string_for_calculation *= float(storage_numerics[j + 1])
            print('string_for_calculation in second "*" -> ', string_for_calculation)
    elif storage_sign[j] == '+' and type(storage_numerics[j]) == int:
        string_for_calculation += int(storage_numerics[j + 1])
        print('string_for_calculation in "+" -> ', string_for_calculation)
    else:
        string_for_calculation += float(storage_numerics[j + 1])
        print('string_for_calculation in "+" -> ', string_for_calculation)
print('string_for_calculation -> ', string_for_calculation)

