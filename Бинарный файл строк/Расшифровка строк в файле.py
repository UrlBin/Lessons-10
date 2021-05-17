'''
Введенные строки
dasgfag
4errfv34
afsf
sd
ffc34
'''

file_name = input('Введите название файла. Если название не введено, то будет открыт ранее созданный файл.')
if not file_name:
    file_name = 'binary_string.bin'

with open(file_name, mode='rb') as opened_file:
    number_of_lines = int.from_bytes(opened_file.read(4), byteorder='little')
    print(f'В прочитанном фале {number_of_lines} строк.')
    for i in range(0, number_of_lines):
        output_string = ''
        length_of_next_line = int.from_bytes(opened_file.read(4), byteorder='little')
        print(f'Длина строки № {i + 1} - {length_of_next_line} символов.')
        for j in range(0, length_of_next_line):
            output_string += chr(int.from_bytes(opened_file.read(2), byteorder='little'))
        print(f"Значение строки № {i + 1} из файла -> ", output_string)
