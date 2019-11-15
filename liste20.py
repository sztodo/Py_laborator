def my_function(s,sub):
    print(s.count(sub))


def my_function_list(my_list, strg):
    for string in my_list:
        my_function(string, strg)


if __name__ == '__main__':
    my_list = ['Python și PyCharm', 'Monty Python and the Holy Grail', '']
    strg = 'Py'
    my_function_list(my_list, strg)
