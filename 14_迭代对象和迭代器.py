# _*_coding:utf-8_*_
# Author:liu

from collections import Iterable
from collections import Iterator

'''
    list typle str set等都是可迭代对象
    isinstance:判断是否是可迭代对象
    Iterable:可迭代对象
    Iterator:迭代器
            可以使用next()函数取值的迭代对象是迭代器
            生成器一定是迭代器
            使用迭代器取值
'''


def main():
    info = [x for x in range(10)]

    print(info)
    # 判断指定的数据是否为指定的类型  Iterable->可迭代对象
    # 判断是否是可迭代对象
    result = isinstance(info, Iterable)
    print('是否可迭代对象：', result)

    # 判断是否是迭代器 list tuple set dict str 都不是迭代器
    result = isinstance([], Iterator)
    print('是否迭代器：', result)
    result = isinstance({}, Iterator)
    print('是否迭代器：', result)
    result = isinstance("3", str)
    print(result)
    print('----------')
    # 使用iter函数转成迭代器
    result = isinstance(iter([]), Iterator)
    print('是否迭代器:', result)
    print('--' * 100)
    # 使用iter函数创建迭代器
    iterator_info = iter([1, 2, 3, 5, 7, 8])
    # 使用next()取值
    info = next(iterator_info)
    print(info)
    info = next(iterator_info)
    print(info)
    info = next(iterator_info)
    print(info)


if __name__ == '__main__':
    main()
