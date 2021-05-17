'''
Введенные строки
dasgfag
4errfv34
afsf
sd
ffc34
'''

file_name = 'binary_string.bin'

with open(file_name, mode='rb') as opened_file:
    while True:
        number_of_lines = opened_file.read(4)
        if not number_of_lines:
            break
        else:
            print("Декодированное число из файла --- ", int.from_bytes(line, byteorder='little'))