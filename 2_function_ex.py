def print_my_name(name, dish='pasta'):
    """
    dummy funtion that prints the name
    :param name:
    :return: nothing
    """
    print('Hi Welcome ' + name)
    print('Please eat ', dish)


def sum_of_list(list):
    return sum(list)


print_my_name('Akshay', 'Samosa')


print(sum_of_list([1, 2, 3, 4, 5]))


def my_fun():
    def foo():
        print('From foo')
    return foo()

my_fun()