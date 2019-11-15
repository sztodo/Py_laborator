def my_function(s):
    print(s[2::3]*20)

def my_function_list(my_list):
    for string in my_list:
        my_function(string)

if __name__ == '__main__':
    my_list = ['abc', 'abcdde']
    my_function_list(my_list)
