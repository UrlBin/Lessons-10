storage_list = []
date = ''
time = ''
while  True:
    number_of_names = input("Введите количество вводимых имен, кому планируется выслать приглашения: ")
    if number_of_names.isdigit():
        for i in range(0, int(number_of_names)):
            input_names = input("Введите имя: ")
            storage_list.append(input_names)
        break
    else:
        print("Введены не корректные данные")

date = input("Введите дату мероприятия: ")
time = input("Введите время мероприятия: ")

for i in range(0, int(number_of_names)):
    with open(f'{storage_list[i]}.txt', mode='w', encoding='utf-8') as file:
        file.write(f'Привет, {storage_list[i]}! Приглашаем тебя на наш\n'
                   f'школьный концерт {date} в {time}!\n'
                   f'С уважением, Администрация.')