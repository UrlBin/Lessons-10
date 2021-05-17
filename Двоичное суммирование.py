input_path = input("Введите путь к файлу, где записаны числа в двоичном виде,\n"
                   "если путь не указан, то поиск будет произведен в другой папке - ")
name_of_file = 'Псевдослучайная последовательность/psypho.bin'


with open(name_of_file, mode='rb') as opened_file:
    number_one = opened_file.read(4)
    print('Первое число из файла - ', int.from_bytes(number_one, byteorder='little'))
    number_two = opened_file.read(4)
    print('Второе число из файла - ', int.from_bytes(number_two, byteorder='little'))
    sum_of_two_numbers = int.from_bytes(number_one, byteorder='little') + int.from_bytes(number_two, byteorder='little')
    print("Результат двоичного суммирования прочитанных - ", sum_of_two_numbers)
