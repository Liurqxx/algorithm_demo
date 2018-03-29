# _*_coding:utf-8_*_
# Author:liu
from matplotlib import pyplot
import numpy


def zhexiantu():
    '''折线图'''
    # 创建数据列表
    num_list = [1, 6, 8, 3, 4, 2, 7, 6]
    num_list2 = [7, 5, 8, 3, 6, 2, 8, 1]
    # 将数据添加到图表中
    # 调节线条粗细和颜色
    pyplot.plot(num_list, num_list2, linewidth=6, c='red')
    # 设置x,y标签和大小
    pyplot.xlabel('X', fontsize=16)
    pyplot.ylabel('Y', fontsize=16)
    # 设置刻度数字的大小
    pyplot.tick_params(axis='bot', lablesize=10)
    # 设置图表大标题
    pyplot.title('number')
    # 显示图表
    pyplot.show()


# 柱状图
def zhifangtu():
    '''直方图'''

    mu = 100

    sigma = 20

    x = mu + sigma * numpy.random.randn(20000)  # 样本数量

    pyplot.hist(x, bins=100, color='green', normed=True)  # bins显示有几个直方,normed是否对数据进行标准化

    pyplot.show()


def zhuzhuantu():
    '''柱状图'''

    y = [20, 10, 30, 25, 15]

    index = numpy.arange(5)
    print(index, type(index))
    pyplot.bar(left=index, height=y, color='green', width=0.5)

    pyplot.show()


def sandiantu():
    '''散点图'''

    x = numpy.random.randn(1000)

    y = x + numpy.random.randn(1000) * 0.5

    pyplot.scatter(x, y, s=5, marker='<')  # s表示面积，marker表示图形

    pyplot.show()


def bingzhuangtu():
    '''饼状图'''
    # 分类名
    labels = 'A', 'B', 'C', 'D'
    # 分类数据
    fracs = [15, 30, 45, 10]

    pyplot.axes(aspect=1)  # 使x y轴比例相同

    explode = [0, 0.05, 0, 0]  # 突出某一部分区域

    pyplot.pie(x=fracs, labels=labels, autopct='%.0f%%', explode=explode)  # autopct显示百分比

    pyplot.show()


def xiangxingtu():
    '''箱形图'''
    numpy.random.seed(100)
    data = numpy.random.normal(size=(1000, 4), loc=0, scale=1)

    labels = ['A', 'B', 'C', 'D']

    pyplot.boxplot(data, labels=labels)

    pyplot.show()


def main():
    # 折线图
    # zhexiantu()
    # 直方图
    # zhifangtu()
    # 柱状图
    # zhuzhuantu()
    # 散点图
    # sandiantu()
    # 饼状图
    # bingzhuangtu()
    # 箱形图
    xiangxingtu()


if __name__ == '__main__':
    main()
