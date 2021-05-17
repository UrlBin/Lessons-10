'''
Введенные строки
dasgfag
4errfv34
afsf
sd
ffc34
'''

commands_list = []
list_of_strings = []
output_list_of_strings = bytes()
file_name = 'binary_string.bin'

print("Введите строку, состоящую из ASCII символов.\n"
      "Окончанием ввода строк - будет ввод пустой строки.\n")
while True:
    input_one_command = input()
    if input_one_command:
        commands_list.append(input_one_command.strip())
    else:
        break

length_of_list = (len(commands_list).to_bytes(4, byteorder='little'))
list_of_strings.append(length_of_list)
for i in commands_list:
    length_of_string = (len(i).to_bytes(4, byteorder='little'))
    list_of_strings.append(length_of_string)
    for j in i:
        one_element = ord(j).to_bytes(2, byteorder='little')
        list_of_strings.append(one_element)

for j in list_of_strings:
    output_list_of_strings += j

with open(file_name, mode='wb') as file:
    file.write(output_list_of_strings)
