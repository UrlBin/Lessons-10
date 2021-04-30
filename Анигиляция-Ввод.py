veshestvo = list()
anti_veshestvo = list()
my_mnozhestvo = set()

#Ввод заданных параметров
my_number_i = int(input('Введите натуральное цисло N - количества веществ: '))
while my_number_i > 0:
    veshestvo.append(input('Введите название вещества: '))
    my_number_i -= 1
print(veshestvo)

my_number_j = int(input('Введите натуральное цисло N - количества антивеществ: '))
while my_number_j > 0:
    anti_veshestvo.append(input('Введите название антивещества: '))
    my_number_j -= 1
print(anti_veshestvo)

#Процесс аннигиляции
for i in veshestvo:
    count = 0
    if i in anti_veshestvo:
        veshestvo.remove(i)
        anti_veshestvo.remove(i)
    count += 1

for i in anti_veshestvo:
    count = 0
    if i in veshestvo:
        veshestvo.remove(i)
        anti_veshestvo.remove(i)
    count += 1

#Убирает повторяющийся оставшиеся компонентыпосле анигиляции
for i in range(0, len(veshestvo)-1):
    count = 0
    value = veshestvo[i]
    count = veshestvo.count(value)
    while count != 1:
        veshestvo.remove(value)
        count -= 1

for i in range(0, len(anti_veshestvo)-1):
    count = 0
    value = anti_veshestvo[i]
    count = anti_veshestvo.count(value)
    while count != 1:
        anti_veshestvo.remove(value)
        count -= 1

#Объединяем два списка оставшихся компонентов в один список
my_answer = list(veshestvo + anti_veshestvo)

print("После проведенного анализа, наибольшее число согласных у слова: ", my_answer)