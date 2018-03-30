# _*_coding:utf-8_*_
# Author:liu
'''
    输入一个整数n，输出整数n相邻最近的两个素数
    如果左右素数距离相同，则输出左侧素数以及相应的距离
    如果整数n本身是素数，则输出自己本身，距离为0
'''
#记录距离
min_long = 0
#记录数值
min_num = 0


def main():
    global min_long
    global min_num
    in_num = int(input("请输入一个整数:"))

    fron_size = 0
    #得到左边的距离
    for front_num in range(in_num, 1, -1):
        front_result = is_sushu(front_num)
        if not front_result:
            min_long = fron_size
            min_num = front_num
            print('左边距离:', fron_size)
            break
        else:
            fron_size += 1

    size = 0
    #得到右边的距离
    while True:
        result = is_sushu(in_num)
        # 是素数
        if not result:
            print('右边距离:', size)
            if size < min_long:
                print('最短距离：', size, '素数：', in_num)

            else:
                print('最短距离:', min_long, '素数:', min_num)
            break
        else:
            size += 1
            in_num += 1


# 判断是不是素数
def is_sushu(num):
    for i in range(2, num):
        if num % i == 0:
            return 1
    return 0


if __name__ == '__main__':
    main()
