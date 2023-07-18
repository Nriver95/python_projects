def myFun(*args):
    for arg in args:
        print(arg)

myFun('This is an example of args', 'string', 'and then an integer', 5)


def noFun(**kwargs):
        print('kwargs', kwargs)

noFun(first = "1", second = "2", third = "3")
