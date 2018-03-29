# _*_coding:utf-8_*_
# Author:liu
'''
    输入一个整数n，判断整数n是不是一些数（这些数是正数且不重复）的阶乘
    例如：9=1!+2!+3!
    如果是输出yes，不是则输出no
'''

sum = 0
num2 = 0
num_list = []


def main():
    global num2
    num2 = int(input("请输入一个正整数:"))

    res = count_num(num2)
    if res == num2 and len(set(num_list)) == len(num_list):
        # print(num_list)
        print('YES')
    else:
        # print(num_list)
        print('NO')


def count_num(num):
    # 9 = 1!+2!+3!
    global sum
    global num2
    global num_list

    for one_num in range(num, 0, -1):
        # 阶乘结果
        jiechegn_result = jiecheng(one_num)
        if jiechegn_result == 1:
            num_list.append(1)
            return 1
        # 如果阶乘结果小于传入的数
        elif jiechegn_result < num:
            sum += jiechegn_result
            num_list.append(jiechegn_result)
            return jiechegn_result + count_num(num2 - sum)


# 求阶乘
def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n - 1)


if __name__ == '__main__':
    main()
