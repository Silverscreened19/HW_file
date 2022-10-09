cook_book = {}


with open('data.txt', 'rt') as file:
    for dish_name in file:
        dish = dish_name.strip()
        recipy = []
        persons_count = file.readline()
        for i in range(int(persons_count)):
            person = file.readline()
            ingredient, quantity, unit = person.strip().split(" | ")
            recipy.append({"ingredient_name": ingredient,
                          "quantity": quantity,
                           "measure": unit})
        blank_line = file.readline()
        cook_book[dish] = recipy

print(cook_book)


dishes = list(cook_book.keys())


def get_shop_list_by_dishes(dishes, person_count):

    result = {}
    for dish in dishes:
        if dish in dishes:
            recipy = cook_book[dish]
            for element in recipy:
                ingredient = element['ingredient_name']
                quantity = int(element['quantity']) * person_count
                if ingredient not in result.keys():
                    measure = element['measure']
                    result[ingredient] = {'measure': measure,
                                          'quantity': quantity}
                else:
                    quantity += quantity
                    measure = element['measure']
                    result[ingredient] = {'measure': measure,
                                          'quantity': quantity}
    print(result)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)

with open('1.txt', 'rt') as file:
    file_1_list = file.readlines()
    file_1_len = (len(file_1_list))
    file_1 = ' '.join(file_1_list)


with open('2.txt', 'rt') as file:
    file_2_list = file.readlines()
    file_2_len = (len(file_2_list))
    file_2 = ' '.join(file_2_list)


with open('3.txt', 'rt') as file:
    file_3_list = file.readlines()
    file_3_len = (len(file_3_list))
    file_3 = ' '.join(file_3_list)


my_list = []
dic_common = {
    file_1_len: ['1.txt', file_1],
    file_2_len: ['2.txt', file_2],
    file_3_len: ['3.txt', file_3]
    }

dic_common = dict(sorted(dic_common.items()))


with open('res.txt', 'w') as file:
    for key in dic_common.keys():
        my_list.append(key)
    my_list = sorted(my_list)
    for key in dic_common.keys():
        if key == min(my_list):
            file.writelines(f'{dic_common[key][0]}\n{key}\n'
                            f'{dic_common[key][1]}')
        elif key == max(my_list):
            file.writelines(f'{dic_common[key][0]}\n{key}\n'
                            f'{dic_common[key][1]}')
        else:
            file.writelines(f'{dic_common[key][0]}\n{key}\n'
                            f'{dic_common[key][1]}')
