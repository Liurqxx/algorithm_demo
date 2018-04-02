# _*_coding:utf-8_*_
# Author:liu
import gevent
from gevent import monkey
import time

# 打补丁，让程序能够识别系统的耗时操作以及网络资源请求的耗时操作
monkey.patch_all()


def work1():
    # 获取当前协程
    print(gevent.getcurrent())
    while True:
        print('---work1----')
        time.sleep(0.5)


def work2():
    while True:
        print('----work2----')
        time.sleep(0.5)


def main():
    # 创建协程
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 主线程等待协程结束后才结束
    g1.join()
    g2.join()


if __name__ == '__main__':
    main()
