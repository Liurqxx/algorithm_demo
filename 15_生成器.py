# _*_coding:utf-8_*_
# Author:liu
'''
    生成器：减轻内存占用情况
    保存算法，何时用何时取

'''


# 方式二：使用yield
def creatNum():
    # 创建生成器
    a, b = 0, 1
    for i in range(10):
        # 函数停止在yield处，返回b的数值
        temp = yield b
        print('temp:', temp)
        a, b = b, a + b


def main():
    # 创建列表生成式,如果数值过大，内存资源耗费特别大，使用生成器改善
    info = [x * 2 for x in range(10)]
    print(info)

    # 方式一：创建列表生成器,返回一个生成器对象
    info = (x * 2 for x in range(100000))
    print(info)
    # 使用next()取值
    print(next(info))


if __name__ == '__main__':
    main()
    # 创建生成器对象
    c = creatNum()
    # 使用next取值
    print(next(c))
    # 遍历生成器对象取值
    for i in c:
        print(i)
    # 给生成器赋值
    # c.send('hahh')
