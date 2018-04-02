# _*_coding:utf-8_*_
# Author:liu
'''
    水仙花数：各个位数的立方和等于它本身
'''


def main():
    n = int(input("请输入一个整数(100<n<1000):"))
    num1 = n // 10
    num2 = num1 % 10
    num3 = n // 100
    num4 = n % 10

    if (num3 ** 3) + (num2 ** 3) + (num4 ** 3) == n:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
