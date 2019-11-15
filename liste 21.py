def my_function(s):
    l = s.split(' ')
    l = l[-1::-1]
    s = " ".join(l)
    print(s)


def my_function_list(my_list):
    for string in my_list:
        my_function(string)


if __name__ == '__main__':
    my_list = ['Python si Pycharm', 'Foarte Frumos', 'Bravo']
    my_function_list(my_list)
