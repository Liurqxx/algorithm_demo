# _*_coding:utf-8_*_
# Author:liu


import urllib.request
import time
import gevent
from gevent import monkey

'''
    使用gevent下载多张图片
'''
# 打补丁
monkey.patch_all()


# 下载图片
def down_img(img_url, img_name):
    try:
        # 网页获取图片数据资源
        response = urllib.request.urlopen(img_url)

        with open(img_name) as img_file:
            # 读取网络数据
            while True:
                img_data = response.read(1024)
                if img_data:
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print("图片下载异常")
    else:
        print("图片下载完成")


def main():
    # 准备图片地址
    img_url1 = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=551346117,2593226454&fm=27&gp=0.jpg"
    img_url2 = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=829730016,3409799239&fm=27&gp=0.jpg"
    img_url3 = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1815077192,817368579&fm=27&gp=0.jpg"

    # 创建协程开始下载图片
    # 主线程等待所有的协程结束后才结束
    gevent.joinall([
        gevent.spawn(down_img, img_url1, '1.jpg'),
        gevent.spawn(down_img, img_url2, '2.jpg'),
        gevent.spawn(down_img, img_url3, '3.jpg')
    ])


if __name__ == '__main__':
    main()
