# text = 'пример вводимой строки'

a = tuple()

text = input('Введите строку для обработки, в нижнем регистре: ')
a = tuple(text)
b = dict()


for i in a:
    count = a.count(i)
    b[i] = count

for j, k in b.items():
    print('\'', j, '\'', ' : ', k, sep='')

