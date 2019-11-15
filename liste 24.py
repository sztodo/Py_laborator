def my_function(s,n):
    s = s[:len(s)-n] + s[len(s)-n:].lower()
    print(s)


def my_function_list(my_list, numbr):
    for string in my_list:
        my_function(string, numbr)


if __name__ == '__main__':
    my_list = ['RTGCS', 'BABY GOT BACK', 'QUIRCKY', 'idanDEd']
    numbr = 3
    my_function_list(my_list, numbr)
