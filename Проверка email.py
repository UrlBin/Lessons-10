# вводимая строка - asd@asd.ru

out_put_error = 'ОШИБКА'
out_put_ok = 'ОК'
condition = 0

input_string = input('Введите email для его проверки: ')

first_part, union_second_parts = input_string.split('@')
# print(first_part, union_second_parts)

second_one, second_two = union_second_parts.split('.')
# print(second_one, second_two)

if len(first_part) < 1 or len(second_one) < 1 or len(second_two) < 1 \
        or not first_part.isalnum() or not second_one.isalnum() or not second_two.isalpha():
    print(out_put_error)
    condition = 1

if condition != 1:
    for i in first_part:
        if i.isupper():
            print(out_put_error)
            condition = 1
            break
if condition != 1:
    for j in second_one:
        if j.isupper():
            print(out_put_error)
            condition = 1
            break
if condition != 1:
    for k in second_two:
        if k.isupper():
            print(out_put_error)
            condition = 1
            break

if condition == 0:
    print(out_put_ok)