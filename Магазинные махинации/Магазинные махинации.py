'''
Данные в файле:
Молоко, 50; 50
Яйцо, 5; 10000
Масло, 150; 100
Хлеб, 10.5; 105

Вводимые команды:
ИЗМЕНИТЬ ЦЕНА Масло 130
ИЗМЕНИТЬ КОЛВО Молоко 110
ИЗМЕНИТЬ ИМЯ Яйцо Яйцо_куриное
УДАЛИТЬ Хлеб
'''

commands_list = []
db_name = 'shop_db.txt'
list_of_string = []
output_list = []

print("Введите команду, введенная пустая строка позволит закончить ввод:")
while True:
    input_one_command = input("")
    if input_one_command:
        commands_list.append(input_one_command.split())
        # print(commands_list)
    else:
        break
# print(len(commands_list))
file = open(db_name, mode='r', encoding='utf-8')

for j in file.readlines():
    j = j.replace(' ', '').strip().split(';')
    list_of_string.append([j[0].split(','), j[1]])
    # print(output_list)
file.close()

for i in commands_list:
    for j in list_of_string:
        if i[0] == 'ИЗМЕНИТЬ' and i[1] == 'ЦЕНА':

            if j[0][0] == i[2]:
                text = j[0][0] + ', ' + i[3] + '; ' + j[1] + '\n'
                output_list.append(text)
                # count += len(text)
                # file.seek(count)
            # else:
            #     text = list_of_string[j][0][0] + ', ' + list_of_string[j][0][1] + '; ' + list_of_string[j][1] + '\n'
            #     output_list.append(text)
            #     # count += len(text)
            #     # file.seek(count)

        elif i[0] == 'ИЗМЕНИТЬ' and i[1] == 'КОЛВО':

            if j[0][0] == i[2]:
                text = j[0][0] + ', ' + j[0][1] + '; ' + i[3] + '\n'
                output_list.append(text)
                # count += len(text)
                # file.seek(count)
            # else:
            #     text = list_of_string[j][0][0] + ', ' + list_of_string[j][0][1] + '; ' + list_of_string[j][1] + '\n'
            #     output_list.append(text)
            #     # count += len(text)
            #     # file.seek(count)

        elif i[0] == 'ИЗМЕНИТЬ' and i[1] == 'ИМЯ':

            if j[0][0] == i[2]:
                text = i[3] + ', ' + j[0][1] + '; ' + j[1] + '\n'
                output_list.append(text)
                # count += len(text)
                # file.seek(count)
            # else:
            #     text = list_of_string[j][0][0] + ', ' + list_of_string[j][0][1] + '; ' + list_of_string[j][1] + '\n'
            #     output_list.append(text)
            #     # count += len(text)
            #     # file.seek(count)

        elif i[0] == 'УДАЛИТЬ':

            if j[0][0] == i[1]:
                continue
            else:
                text = j[0][0] + ', ' + j[0][1] + '; ' + j[1] + '\n'
                output_list.append(text)
            #     # count += len(text)
            #     # file.seek(count)
        else:
            text = list_of_string[j][0][0] + ', ' + list_of_string[j][0][1] + '; ' + list_of_string[j][1] + '\n'
            output_list.append(text)
            # count += len(text)
            # file.seek(count)

with open(db_name, mode='w', encoding='utf-8') as file:
    for k in output_list:
        file.write(k)