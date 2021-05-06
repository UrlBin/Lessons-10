# Вводимые строки: Abbccc, AaAAAabcdEddEEEee
input_string = input('Введите строку из латинских букв в разном регистре: ')

if not input_string:
    print('Вы ни чего не ввели, повторите еще раз.')

output_string = ''
count = 1
for i in range(0, len(input_string)):
    if i + 1 == len(input_string):
        if count == 1:
            output_string += input_string[-1].lower()
        else:
            output_string += str(count) + input_string[-1].lower()

    elif input_string[i].lower() != input_string[i + 1].lower():
        if count == 1:
            output_string += input_string[i].lower()
        else:
            output_string += str(count) + input_string[i].lower()
            count = 1
    else:
        count += 1
        print(count)

print(output_string)