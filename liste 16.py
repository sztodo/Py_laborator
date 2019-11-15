def my_function(s):
    print(''.join(sorted(s)))

def my_function_list(my_list):
    for string in my_list:
        my_function(string)

if __name__ == '__main__':
    my_list = ['dcbaa', 'Excelent lucrat!', 'Python', '']
    my_function_list(my_list)
