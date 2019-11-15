def my_function(my_string):
    print(float(my_string) ** 3)


def my_function_list(my_list):
    for string in my_list:
        my_function(string)


if __name__ == '__main__':
    my_list = ['2', '2.5', '0']
    my_function_list(my_list)
