# Выражение для ввода - 1+2*3*4+5      1 + 2 *  3 * 4  + 5.0   1+2*3*4+5+6+7*8+9
string_for_calculation = ''

# input_string = input('Введите строку для парсинга арифметических выражений: ')

while True:
    input_string = input('Введите строку для парсинга арифметических выражений: ')
    if len(input_string) < 3 or input_string.find('+') == - 1 or input_string.find('*') == - 1:
        print('Вы ввели не корректное выражение. ')
    else:
        break
        # print('storage_numerics', storage_numerics)

# Сортировка в отдельные списки цифр и знаков арифметических выражений.
storage_numerics = []
storage_sign = []

number = ''
for i in range(0, len(input_string)):
    if input_string[i] == ' ' and not storage_numerics:
        continue
    elif input_string[i].isdigit() or input_string[i] == '.':
        number += input_string[i]
        if i == len(input_string) - 1:
            if number != '':
                storage_numerics.append(number)
                break
            else:
                break
    elif input_string[i] == ' ' and storage_numerics:
        if number != '':
            storage_numerics.append(number)
            number = ''
        else:
            continue
    elif input_string[i] == '*' or input_string[i] == '+':
        if number != '':
            storage_sign.append(input_string[i])
            storage_numerics.append(number)
            number = ''
        else:
            storage_sign.append(input_string[i])

print('storage_numerics', storage_numerics)
print('storage_sign', storage_sign)

# Сведение всех элементов в один список
answer_string = list()
for j in range(0, len(storage_numerics)):
    answer_string.append(storage_numerics[j])
    if j != len(storage_sign):
        answer_string.append(storage_sign[j])

# print('answer_string', answer_string)

# Выполнение арифметических действий.

while len(answer_string) != 1:
    for p in answer_string:
        index_p = answer_string.index(p)

        if p == '*' and index_p <= len(answer_string) - 2:
            if len(answer_string) == 3:
                answer_string[index_p - 1] = int(answer_string[index_p - 1]) * \
                                             int(answer_string.pop(index_p + 1))
                answer_string.pop(answer_string.index(p))
                # print('First answer_string in if "+" (int) -> ', answer_string)
                # break
            elif str(answer_string[index_p - 1]).isdecimal() and \
                    str(answer_string[index_p + 1]).isdecimal():
                answer_string[index_p - 1] = int(answer_string[index_p - 1]) * \
                                             int(answer_string.pop(index_p + 1))
                answer_string.pop(answer_string.index(p))
                # print('First answer_string in if "*" (int) -> ', answer_string)
            else:
                answer_string[index_p - 1] = float(answer_string[p - 1]) * \
                                             float(answer_string.pop(index_p + 1))
                answer_string.pop(answer_string.index(p))
                answer_string.pop(answer_string.index(p))
                # print('First answer_string in else "*" (float) -> ', answer_string)
        elif p == '+' and index_p <= len(answer_string) - 2:

            if len(answer_string) == 3:
                if str(answer_string[index_p - 1]).isdecimal() and str(answer_string[index_p + 1]).isdecimal():
                    answer_string[index_p - 1] = int(answer_string[index_p - 1]) + \
                                                 int(answer_string.pop(index_p + 1))
                    answer_string.pop(answer_string.index(p))
                else:
                    answer_string[index_p - 1] = float(answer_string[index_p - 1]) + \
                                                 float(answer_string.pop(index_p + 1))
                    answer_string.pop(answer_string.index(p))
                # print('First answer_string in if "+" (int) -> ', answer_string)
                # break
            elif answer_string[index_p + 2] != '*':
                if str(answer_string[index_p - 1]).isdecimal() and \
                        str(answer_string[index_p + 1]).isdecimal():
                    answer_string[index_p - 1] = int(answer_string[index_p - 1]) + \
                                                 int(answer_string.pop(index_p + 1))
                    answer_string.pop(answer_string.index(p))
                    # print('First answer_string in if "+" (int) -> ', answer_string)

                else:
                    answer_string[index_p - 1] = float(answer_string[index_p - 1]) + \
                                                 float(answer_string.pop(index_p + 1))
                    answer_string.pop(answer_string.index(p))
                    # print('First answer_string in else "+" (float) -> ', answer_string)

print('\n', 'Ответ -> ', answer_string[0], sep='')
# Проверка через передачу строки в функцию "eval()"
print('Checked by "eval()" function (it is very short and very danger solution) -> ', eval(input_string))

