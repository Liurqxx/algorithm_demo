# _*_ coding:utf-8 _*_
# Author:liu
'''
    菲波那切数列递推公式：
        f(n) = f(n-1) + f(n-2)
'''


def tony(num):
    '''递推公式'''
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num > 2:
        return tony(num - 1) + tony(num - 2)


def main():
    in_num = int(input("请输入你要计算的值:"))
    #遍历输入的数值
    for number in range(1, in_num + 1):
        print(tony(number), "\t", end="")


if __name__ == '__main__':
    main()
