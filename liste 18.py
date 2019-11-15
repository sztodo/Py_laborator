def my_function(s):
    print(s.startswith("Mulțumesc"))


def my_function_list(my_list):
    for string in my_list:
        my_function(string)


if __name__ == '__main__':
    my_list = ['Mulțumesc frumos!', 'Foarte frumos', 'Mulțumesc']
    my_function_list(my_list)
