def my_function(s,sub):
    print(s.count(sub))


def my_function_list(my_list, strg):
    for string in my_list:
        for i in strg:
            my_function(string, i)


if __name__ == '__main__':
    my_list = ['Python și PyCharm', 'Monty Python and the Holy Grail', '']
    strg = ['Py', 'th']
    my_function_list(my_list, strg)
