import random

# The first test sets created given by the assignment
test = ['a', ['b', 'b'], [['c', ['b']], 'a']]
hard_list = ['a', 'b', ['a', ['g', 'c', ['k'], 'p', ], 't'],
             'f', 'q', [['g', ['y']], 'c', ['k'], 'p', ], 't']


def make_list(n_of_elements, new_list_chance, elements):
    '''A helper function for creating arbitrary lists for testing, max length set as 10 and with reasonable depth'''
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
    '''Wrapper function for creating the arbitrary lists with input arguments
       strings: the characters we want to insert into the lists
       n_of_elements: the length of the lists, could be anything from 0,10
       new_list_chance: the chance of creating another depth of lists
    '''
    strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    n_of_elements = random.randint(0, 10)
    new_list_chance = 0.75

    return make_list(n_of_elements, new_list_chance, strings)


def flatten(old_list):
    '''Flatten a given nestled list with arbitrary depths'''
    new_list = []
    if old_list is not None:
        element = old_list[0]
        if isinstance(element, list):
            new_list.extend(flatten(element))
        else:
            new_list.extend(element)
        if len(old_list) > 1:
            new_list.extend(flatten(old_list[1:]))

        return new_list


# Test 100 cases of arbitrary created lists, print every 10th list to see the results
# Check if anyone fails and print that list to investigate
for i in range(100):
    test_list = make_aribtrary_list()
    flattened_list = flatten(test_list)
    if flattened_list is None:
        print('Test list was: {} \n Flattened failed, list became: {}'.format(
            test_list, flattened_list))
    if(i % 10 == 0):
        print('Test list was: {} \n Flattened list became: {}'.format(
            test_list, flattened_list))

print(flatten(hard_list))
