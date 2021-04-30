my_list = list()
count_list = list()
second_name = ''
my_mnozhestvo = set()
soglasnie = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}
glasnie = {'а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я'}

my_number = int(input('Введите натуральное цисло N - количества строк: '))
while my_number > 0:
    my_list.append(input('Введите слово: '))
    my_number -= 1
print(my_list)

# Подсчет количества согласных букв
for i in range(0, len(my_list)):
    # print(len(my_list))
    word = list(my_list[i])
    # print(word)
    count = 0
    for j in range(0, len(word)):
        # print(i, ' - значение i')
        # print(j, ' - значение j')
        if word[j] in soglasnie:
            count += 1
    count_list.append(count)
print(count_list)

# Поиск слова с максимальным количеством согласных букв
answer_index=0
new_count = 0
for i in range(0, len(count_list)):
        # print(i)
        if new_count == len(count_list)-1:
            break  
        elif count_list[answer_index] > count_list[i]:
            answer_index = answer_index
        elif count_list[answer_index] == count_list[i]:
            answer_index=answer_index
        else: 
            answer_index = i
        new_count += 1
        

print("После проведенного анализа, наибольшее число согласных у слова: ", my_list[answer_index])