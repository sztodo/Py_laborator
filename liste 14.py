def my_function(my_string, my_strg):
    print(my_string[:my_string.rfind(my_strg)])

def my_function_list(my_list, my_str):
    for string in my_list:
        my_function(string, my_str)

if __name__ == '__main__':
    my_list = ['abababaa', 'ab']
    my_str = 'ab'
    my_function_list(my_list, my_str)
