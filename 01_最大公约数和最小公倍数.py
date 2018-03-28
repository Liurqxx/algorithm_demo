# _*_ coding:utf-8 _*_
# Author:liu

'''
    键盘录入两个正整数，输出最大公约数和最小公倍数
'''


# 求最大公约数
def max_num(num1, num2):
    result = 0
    # 确保num1 < num2
    if num1 > num2:
        num1, num2 = num2, num1
    # 得到最大公约数
    for n in range(1, num1 + 1):
        if num1 % n == 0:
            if num2 % n == 0:
                result = n
    return result


# 最小公倍数
def min_num(num1, num2):
    for n in range(1, num1 + 1):
        if num2 * n % num1 == 0:
            return num2 * n


def main():
    # 键盘录入数据
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数:"))

    # 公约数
    res = max_num(num1, num2)
    print('最大公约数:', res)

    # 公倍数
    res = min_num(num1, num2)
    print('最小公倍数：', res)


if __name__ == '__main__':
    main()
