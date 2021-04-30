a = tuple()
text = input('Введите строку для обработки: ')
b = list()

# text = 'еда_для_буквоежки'
a = tuple(text)

for i in a:
    b.append(i)

while len(b) > 0:
    print(b)
    b.pop(0)
    if len(b) > 1:
        b.pop()

