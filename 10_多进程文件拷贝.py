# _*_coding:utf-8_*_
# Author:liu

import multiprocessing
from multiprocessing import Manager
import os


# 文件拷贝
def file_copy(file_name, file_dir, queue):
    # 创建文件对象
    fw = open(file_dir + '/' + file_name, 'w')
    fr = open(file_name)

    while True:
        # 读取数据
        file_data = fr.read(1024)
        if file_data:
            # 写入数据
            fw.write(file_data)
        else:
            fr.close()
            fw.close()
            # 每拷贝完成一个文件就添加一次
            queue.put(file_name)
            break


if __name__ == '__main__':
    # 创建进程池
    pool = multiprocessing.Pool(3)

    # 输入拷贝的文件路径
    file_path = input("请输入文件路径:")

    # 获取指定目录下的文件列表
    file_list = os.listdir(file_path)
    # 请输入要创建的文件夹
    file_dir = input("请输入要创建的文件夹路径和名称:")
    os.mkdir(file_dir)
    # 创建进程间通信
    queue = Manager().Queue()

    # 循环遍历得到每一个文件
    for file in file_list:
        # 异步开启进程池
        pool.apply_async(file_copy, args=(file, file_dir, queue))

    # 用来显示拷贝进度
    num = 0
    while num < len(file_list):
        # 用来记录拷贝完成了多少文件
        queue.get()
        num += 1
        # 计算百分比
        result = num / len(file_list)
        print('文件拷贝进度:%2.f%%' % (result * 100))
    print("文件拷贝完成...")
    # 关闭进程池
    pool.close()
    # 主进程等待子进程
    pool.join()
