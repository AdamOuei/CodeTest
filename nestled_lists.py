import random

test1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']
test2 = [1, [1, [2, 3]], [[4, [5, 3]], 5, 6], [7, 8, 9]]

test3 = ['a', ['b', 'b'], [['c', ['b']], 'a']]


def make_list(n_of_elements, new_list_chance, elements):
    l = []
    if n_of_elements <= 1:
        return elements[random.randint(0, len(elements)-1)]
    for _ in range(n_of_elements):
        rand = random.random()
        if rand < 0.75:
            new_list = make_list(round(n_of_elements/2),
                                 new_list_chance, elements)
            l.append(new_list)
        else:
            random_char = elements[random.randint(0, len(elements)-1)]
            l.append(random_char)
    return l


def make_aribtrary_list():
    strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    n_of_elements = random.randint(0, 10)
    new_list_chance = 0.75

    return make_list(n_of_elements, new_list_chance, strings)


def flatten(old_list, new_list):
    if old_list is not None:
        element = old_list[0]
        if isinstance(element, list):
            flatten(element, new_list)
        else:
            new_list.append(element)
        if len(old_list) > 1:
            return flatten(old_list[1:], new_list)
        else:
            return new_list


# print(make_aribtrary_list())

for i in range(100):
    test_list = make_aribtrary_list()
    if(i % 10 == 0):

        print('Test list was: {} \n Flattened list became: {}'.format(
            test_list, flatten(test_list, [])))
