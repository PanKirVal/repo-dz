cubes = [x ** 3 for x in range(1000) if x % 2 != 0]
print('Кубы нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list = []
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    print('Числа, деляющиеся на 7: ', my_numbers_sum_list)


cubes = [(x**3)+17 for x in range(1000) if x % 2 == 0]
print('Кубы нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers = []
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    print('Числа, деляющиеся на 7: ', my_numbers_sum_list_even_numbers)