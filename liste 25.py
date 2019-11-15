def my_function(sir,separator):
    b = sir.rsplit(separator,2)
    print(b[0])


def my_function_list(my_list, caracter):
    for string in my_list:
        my_function(string, caracter)


if __name__ == '__main__':
    my_list = ['Python si Pycharm', 'Py Py Py Py', 'Rick and Morty Tv Show']
    caracter = ' '
    my_function_list(my_list, caracter)
