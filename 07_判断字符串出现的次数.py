# _*_coding:utf-8_*_
# Author:liu
'''
    输入两个字符串str1和str2，字符串只能由0和1组成，str1的长度小于str2的长度，
    判断str1在str2中出现的次数
'''


def main():
    str1 = input("输入第一个字符串：")
    str2 = input("输入第二个字符串:")
    count = 0
    for i in range(len(str2) - len(str1)):
        if str2[i:i + len(str1)] == str1:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
