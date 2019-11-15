def my_function(my_string, n):
    print(my_string[:n].lower() + my_string[n:])


def my_function_list(my_list, numbr):
    for string in my_list:
        my_function(string, numbr)


if __name__ == '__main__':
    my_list = ['PYTHON', 'py', 'PyCharm']
    numbr = 2
    my_function_list(my_list, numbr)
