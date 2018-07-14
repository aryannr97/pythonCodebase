import Module

def print_message(string_arg, flag):
    '''
    This function returns concatenated string
    '''

    concatenated_string = string_arg * 3  # works faster than '+' operator as the object size is calculated in advance

    if flag:
        return concatenated_string + '!!!'
    return concatenated_string


def main():
    print ("Hello World")
    print(print_message('Code',True))
    print(print_message('Code Base',False))
    print (Module.foo())

if __name__ == "__main__": # a standard piece of code written when running a .py file directly
    main()


