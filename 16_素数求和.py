# _*_coding:utf-8_*_
# Author:liu

'''
    键盘录入一个整数，求1到该数的所有素数的和
'''


# 判断素数函数
def is_num(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return num


def main():
    # 键盘录入一个整数
    num = int(input("请输入一个整数:"))
    # 记录和
    sum = 0
    for n in range(1, num + 1):
        sum += is_num(n)
    print(sum)


if __name__ == '__main__':
    main()
