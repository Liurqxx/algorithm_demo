# _*_coding:utf-8_*_
# Author:liu
'''
    求一个字符串的最长递增子序列
        ababc->3
'''


def main():
    in_str = input("请输入一个字符串:")
    # in_str = 'ababcceft'
    # 定义一个列表用来保存次数
    list = []
    # 得到每一个元素和对应的索引值
    for index, first_s in enumerate(in_str):
        # 记录次数
        count = 1
        # 定义一个变量用来保存需要判断的字符
        one_str = first_s
        # 用第一个for循环得到的元素跟之后的所有的元素比较，满足条件，count++
        for two_s in in_str[index:]:
            if two_s > one_str:
                # 满足条件
                one_str = two_s
                count += 1
        # 列表内添加每一次的次数
        list.append(count)
    # 排序输出最大值
    list.sort(reverse=True)
    print('最长子字符串的长度:',list[0])


if __name__ == '__main__':
    main()
