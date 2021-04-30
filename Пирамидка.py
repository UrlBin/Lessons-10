row = 3
m = input("Введите символ для рисования пирамиды.")
for i in range(1, row+1):
    print('{:{align}{width}}'.format((' ' + m)*i, align='^', width=row*2))
