# Вводимые данные:
# Молоко, 50; 50
# Яйцо, 10; 10000
# Масло, 150; 100
# Хлеб, 21; 105

storage_list = []
db_name = 'shop_db.txt'
discount = 0.5
condition_for_discount = 100

while  True:
    number_of_product = input("Введите количество вводимых продуктов в базу: ")
    for i in range(0, int(number_of_product)):
        input_product = input("Введите данные по продукту "
                              "в виде <название>, <цена>; <количество_на_складе>: ").replace(' ', '').split(';')
        input_product[0] = input_product[0].split(',')
        storage_list.append(input_product)
        # print(storage_list)
    break

file = open(db_name, mode="a", encoding='utf-8')

for i in range(0, int(number_of_product)):
    if int(storage_list[i][1]) <= condition_for_discount:
        out_string = storage_list[i][0][0] + ', ' + (storage_list[i][0][1]) + \
                     '; ' +  storage_list[i][1] + '\n'
        file.writelines(out_string)
    else:
        out_string = storage_list[i][0][0] + ', ' + str(int(storage_list[i][0][1]) * discount) +\
                     '; ' +  storage_list[i][1] + '\n'
        file.writelines(out_string)
        print(storage_list[i][0][0])

file.close()
