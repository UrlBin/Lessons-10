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
    else:
        break

file = open(db_name, mode='r', encoding='utf-8')
string_acc = file.readlines()
for n in string_acc:
    if n:
        string_from_acc = n.replace(' ', '').strip().split(';')
        list_of_string.append([string_from_acc[0].split(','), string_from_acc[1]])
file.close()

for i in list_of_string:
    for j in commands_list:
        if j[0] == 'ИЗМЕНИТЬ' and j[1] == 'ЦЕНА':

            if i[0][0] == j[2]:
                text = i[0][0] + ', ' + j[3] + '; ' + i[1] + '\n'
                output_list.append(text)

        elif j[0] == 'ИЗМЕНИТЬ' and j[1] == 'КОЛВО':

            if i[0][0] == j[2]:
                text = i[0][0] + ', ' + i[0][1] + '; ' + j[3] + '\n'
                output_list.append(text)

        elif j[0] == 'ИЗМЕНИТЬ' and j[1] == 'ИМЯ':

            if i[0][0] == j[2]:
                text = j[3] + ', ' + i[0][1] + '; ' + i[1] + '\n'
                output_list.append(text)

        elif j[0] == 'УДАЛИТЬ':

            if i[0][0] == j[1]:
                continue
                text = i[0][0] + ', ' + i[0][1] + '; ' + i[1] + '\n'
                output_list.append(text)
            else:
                continue
        else:
            text = list_of_string[i][0][0] + ', ' + list_of_string[i][0][1] + '; ' + list_of_string[i][1] + '\n'
            output_list.append(text)

with open(db_name, mode='w', encoding='utf-8') as file:
    for k in output_list:
        file.write(k)
