def my_function(s):
    s = s.replace('\t', '\n', 1)
    print(s)


def my_function_list(my_list):
    for string in my_list:
        my_function(string)


if __name__ == '__main__':
    my_list = ['Mulțumesc\tfrumos!', 'Foarte frumos!', 'Mulțumesc!\tCu respect,\tStudent']
    my_function_list(my_list)
