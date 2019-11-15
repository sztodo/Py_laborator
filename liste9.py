def my_function_string(s):
    print(s[::2])


def my_function_list(my_list):
    for string in my_list:
        my_function_string(string)


if __name__ == '__main__':
    my_list = ['String!', 'ab']
    my_function_list(my_list)
