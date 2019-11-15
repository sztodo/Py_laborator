def my_function(s):
    s = s.replace('\t', '')
    print(s)


def my_function_list(my_list):
    for string in my_list:
        my_function(string)


if __name__ == '__main__':
    my_list = ['Py\tCharm', 'Py\tth\ton', '\tZ\te\tc\te.', '\t']
    my_function_list(my_list)
