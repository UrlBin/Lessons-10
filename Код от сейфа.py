flag_of_True = 0
number = []
cypher = input('Введите четырехзначный код сейфа (одно четырехзначное натуральное число): ')
cypher_tuple = tuple(cypher)
number_of_numbers = int(input('Введите натуральное число - это количество попыток проверки кода: '))

while number_of_numbers > 0:

    if len(number) < 4:
        number.append(input('Введите одно натуральное число: '))
    else:
        number.append(input('Введите одно натуральное число: '))
    if len(number) >= 4 \
            and number[-1] == cypher_tuple[-1] and number[-2] == cypher_tuple[-2] \
            and number[-3] == cypher_tuple[-3] and number[-4] == cypher_tuple[-4]:
        flag_of_True = 1
    number_of_numbers -= 1

if flag_of_True == 1:
    print('Код верный')
else:
    print('Код неверный')
