def my_function(s):
    print(s[-1::-1])

def my_function_list(my_list):
    for string in my_list:
        my_function(string)

if __name__ == '__main__':
    my_list = ['abcd', 'abc']
    my_function_list(my_list)
