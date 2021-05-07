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
            print('storage_numerics', storage_numerics)
            break
        print('number', number)
    elif input_string[i] == ' ' and not storage_numerics:
        continue
    elif input_string[i] == ' ' and storage_numerics and number != '':
        storage_numerics.append(number)
        print('storage_numerics', storage_numerics)
        number = ''
    else:
        if input_string[i] == '*' or input_string[i] == '+' or input_string[i] == '/' or input_string[i] == '^':
            storage_sign.append(ord(input_string[i]))
        print('storage_sign', storage_sign)
        if number != '':
            storage_numerics.append(number)
            print('storage_numerics', storage_numerics)
        number = ''

for j in range(0, len(storage_numerics)):
    if storage_numerics[j].isdecimal():
        string_for_calculation += f"{int(storage_numerics[j])}"
        if j < len(storage_numerics) - 1:
            string_for_calculation += f"{chr(storage_sign[j])}"

    else:
        string_for_calculation += f"{float(storage_numerics[j])}"
        if j < len(storage_numerics) - 1:
            string_for_calculation += f"{chr(storage_sign[j])}"

print('string_for_calculation', f'{string_for_calculation}')
print('string_for_calculation', f'{string_for_calculation[0]}{string_for_calculation[1]}{string_for_calculation[2]}')

# for j in range(0, len(storage_numerics)):
#     string_for_calculation.join(storage_numerics[j])
#     if j != len(storage_numerics) -1:
#         string_for_calculation.join(str(storage_sign[j]))

print('*: ', ord('*'))
print('+: ', ord('+'))
print('/: ', ord('/'))
print('^: ', ord('^'))