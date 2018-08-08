# _*_coding:utf-8_*_
# Author:liu
import time
import random
import copy

'''
随机生成一个含有5000个元素，每个元素不大于10000的列表,测试不同算法的效率

'''
# 存放每个排序所用到的列表数据，数据相同，id不同
all_list_data = []

# 随机生成5000个100000以内的数值保存到列表内，用于排序计算效率
list_data = [random.randint(0, 100000) for i in range(5000)]

for i in range(9):
    # 把每个相同数据的列表添加到总列表内，使用deepcopy每一个列表，
    # 保证每次执行排序函数使用的数据列表相同
    all_list_data.append(copy.deepcopy(list_data))


# 定义时间装饰器，统计函数运行的时间
def get_time(fun):
    def f(a):
        # 开始时间
        start_time = time.time()
        result = fun(a)
        # 结束时间
        end_time = time.time()

        print('总共耗时：', end_time - start_time)

        return result

    return f


# 冒泡排序
@get_time
def bubble_sort(arry):
    n = len(arry)  # 获得数组的长度
    for i in range(n):
        for j in range(1, n - i):
            if arry[j - 1] > arry[j]:  # 如果前者比后者大
                arry[j - 1], arry[j] = arry[j], arry[j - 1]  # 则交换两者
    return arry
    print('冒泡排序基本---')


# 针对冒泡排序的优化：
# 优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
# 用一个标记记录这个状态即可。
@get_time
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = 1  # 标记
        for j in range(1, n - i):
            if ary[j - 1] > ary[j]:
                ary[j - 1], ary[j] = ary[j], ary[j - 1]
                flag = 0
        if flag:  # 全排好序了，直接跳出
            break
    # return ary
    print('冒泡排序优化1---')


# 优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
@get_time
def bubble_sort3(ary):
    n = len(ary)
    k = n  # k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1, k):  # 只遍历到最后交换的位置即可
            if ary[j - 1] > ary[j]:
                ary[j - 1], ary[j] = ary[j], ary[j - 1]
                k = j  # 记录最后交换的位置
                flag = 0
        if flag:
            break
    # return ary
    print('冒泡排序优化2---')


# 选择排序
@get_time
def select_sort(ary):
    n = len(ary)
    for i in range(0, n):
        min = i  # 最小元素下标标记
        for j in range(i + 1, n):
            if ary[j] < ary[min]:
                min = j  # 找到最小值的下标
        ary[min], ary[i] = ary[i], ary[min]  # 交换两者
    # return ary
    print('选择排序---')


# 插入排序
@get_time
def insert_sort(ary):
    n = len(ary)
    for i in range(1, n):
        if ary[i] < ary[i - 1]:
            temp = ary[i]
            index = i  # 待插入的下标
            for j in range(i - 1, -1, -1):  # 从i-1 循环到 0 (包括0)
                if ary[j] > temp:
                    ary[j + 1] = ary[j]
                    index = j  # 记录待插入下标
                else:
                    break
            ary[index] = temp
    # return ary
    print('插入排序---')


# 希尔排序
@get_time
def shell_sort(ary):
    n = len(ary)
    gap = round(n / 2)  # 初始步长 , 用round四舍五入取整
    while gap > 0:
        for i in range(gap, n):  # 每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while (j >= gap and ary[j - gap] > temp):  # 插入排序
                ary[j] = ary[j - gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap / 2)  # 重新设置步长
    # return ary
    print('希尔排序---')


# 归并排序执行函数
def merge_sort(ary):
    if len(ary) <= 1:
        return ary
    num = int(len(ary) / 2)  # 二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left, right)  # 合并数组


def merge(left, right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l, r = 0, 0  # left与right数组的下标指针
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


# 归并排序
@get_time
def merge_sort_time(ary):
    print('归并排序--')
    merge_sort(ary)


# 快速排功能代码
def quick_sort(ary):
    return qsort(ary, 0, len(ary) - 1)


def qsort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    qsort(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    qsort(alist, low + 1, end)


# 快速排序调用
@get_time
def qsort_time(ary):
    print('快速排序---')
    quick_sort(ary)


# 堆排序功能逻辑
def heap_sort(ary):
    n = len(ary)
    first = int(n / 2 - 1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):  # 构造大根堆
        max_heapify(ary, start, n - 1)
    for end in range(n - 1, 0, -1):  # 堆排，将大根堆转换成有序数组
        ary[end], ary[0] = ary[0], ary[end]
        max_heapify(ary, 0, end - 1)
    return ary


# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary, start, end):
    root = start
    while True:
        child = root * 2 + 1  # 调整节点的子节点
        if child > end:
            break
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1  # 取较大的子节点
        if ary[root] < ary[child]:  # 较大的子节点成为父节点
            ary[root], ary[child] = ary[child], ary[root]  # 交换
            root = child
        else:
            break


# 堆排序调用
@get_time
def heap_time(ary):
    print('堆排序---')
    heap_sort(ary)


if __name__ == '__main__':
    # 快速排序
    qsort_time(all_list_data[7])
    # 冒泡排序基本
    bubble_sort(all_list_data[0])
    # 冒泡排序优化一
    bubble_sort2(all_list_data[1])
    # 冒泡排序优化二
    bubble_sort3(all_list_data[2])
    # 选择排序
    select_sort(all_list_data[3])
    # 插入排序
    insert_sort(all_list_data[4])
    # 希尔排序
    shell_sort(all_list_data[5])
    # 归并合并
    merge_sort_time(all_list_data[6])
    # 堆排序
    heap_time(all_list_data[8])
