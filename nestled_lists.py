import random

test1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']
test2 = [1, [1, [2, 3]], [[4, [5, 3]], 5, 6], [7, 8, 9]]

test3 = ['a', ['b', 'b'], [['c', ['b']], 'a']]


def make_list(l, n_of_elements, new_list_chance, elements):
    print(l)
    print(n_of_elements)

    if n_of_elements == 0:
        print('First')
        return l

    rand = random.random()

    new_list = make_list(l, n_of_elements-1, new_list_chance, elements)
    print(new_list)


def make_aribtrary_list():
    strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    l = []
    n_of_elements = random.randint(0, 10)
    new_list_chance = 0.75

    return make_list(l, n_of_elements, new_list_chance, strings)


print(make_aribtrary_list())


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


print(flatten(test3, []))
