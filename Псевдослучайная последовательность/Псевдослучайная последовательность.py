input_s = input("Введите натуральное число S - семя для генерации псевдослучайной последовательности - ")
input_n = input("Введите натуральное число N - количество элементов последовательности - ")
input_path = input("Введите путь к результирующему файлу, если путь не укзаан, то сохранение будет в текущей папке - ")
pi = list()
name_of_file = 'psypho.bin'

pi.append((int(input_s)))

for i in range(0, int(input_n)):
    pi.append((int(pi[i]) * 1103515245 + 12345) % 32768)
file_name = input_path + name_of_file
with open(file_name, mode='wb') as file:
    for j in pi:
        file.write(j.to_bytes(4, byteorder='little'))
        # print("j.to_bytes(4, byteorder='little')", int(j).to_bytes(4, byteorder='little'))
        # file.write(int(j).to_bytes(4, byteorder='little'))

print("Чтение записанной псевдослучайной последоватеьлности из файла с декодированием и распечаткой каждой строки:")
with open(file_name, mode='rb') as opened_file:
    while True:
        line = opened_file.read(4)
        if not line:
            break
        else:
            print("Декодированное число из файла --- ", int.from_bytes(line, byteorder='little'))

