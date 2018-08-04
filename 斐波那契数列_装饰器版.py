# _*_coding:utf-8_*_
# Author:liu


def func_one(fun):
    def fun(num):
        n, a, b = 0, 0, 1

        while n < num:
            a, b = b, a + b
            n += 1
            print(a, '\t', end="")

    return fun


@func_one
def s_num():
    pass


s_num(100)
