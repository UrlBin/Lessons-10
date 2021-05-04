# input text - '3 4 5@1 2 3@ 3 4 6 9' и '5@7@0'

text = input('Введите строку для обработки: ')

# разделение трех последовательностей цифр
split_text = text.split(sep='@')

# обработка первой последовательности цифр. Нахождение суммы цифр.
sum_of_first_sequence = 0
first_action = split_text[0].split()
for i in first_action:
    sum_of_first_sequence += int(i)

# обработка второй последовательности цифр. Нахождение произведения цифр.
mul_of_second_sequence = 1
second_action = split_text[1].split()
for j in second_action:
    mul_of_second_sequence *= int(j)

# обработка третьей последовательности цифр. Целочисленное деление каждой цифры на 3.
integer_division_of_third_sequence = ''
third_action = split_text[2].split()

for k in third_action:
    integer_division_of_third_sequence += ''.join([str(int(float(k)//3)), '-'])
integer_division_of_third_sequence = integer_division_of_third_sequence.rstrip('-')

print(sum_of_first_sequence, ', ', int(mul_of_second_sequence), ', ',
      integer_division_of_third_sequence, sep='')