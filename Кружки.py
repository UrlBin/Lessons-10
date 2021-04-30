# Программа рассчет учеников, которые посещают только три кружка.

# Основная функция выбора. Сдесь только определяется, а вызывается ниже, в теле программы.
def func_kruzhki(spisok):
    print(spisok[0], spisok[1], spisok[2], '\n', spisok)
    list_spisok = spisok.split('\n')
    print(list_spisok)
    int_number = int(spisok[0])
    my_mnozhestvo = set()
    while int_number > 0:
        second_name = spisok[int_number-1]
        my_mnozhestvo.add(second_name)
        int_number -= 1
    return my_mnozhestvo

# Основной цикл работы прораммы. Работает только при вызове самого файла.
if __name__ == '__main__':
    spisok = '''8
             Маслов
             Хлебов
             Колбасов
             Хлебов
             Хдебов
             Маслов
             Хлебов
             Маслов'''
    proverka_vihoda = 1 # "1" - продолжаем ввод, "0" - выход из цикла
    while proverka_vihoda:
        print("После проведенного анализа, только три кружка посещают: ", func_kruzhki(spisok))
        proverka_vihoda = int(input("Введите \"1\", чтобы продолжить поиск, \"0\" если хотите завершить программу: "))
    print("Проверка закончена. Спасибо что выбрали нашу программу.")
    ball = int(input('Оцените качество нашей программы по шкале от 1 до 10: '))
    if ball >= 6:
        print('Спасибки. Ты лучший! Как и мы.')
    if ball < 6:
        print('Спасибо. Мы будем стараться улучшить наш продукт.')

