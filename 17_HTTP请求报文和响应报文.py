# _*_coding:utf-8_*_
# Author:liu
import socket
import re



'''
响应报文:
    响应行：
    HTTP/1.1 200 OK
        格式：HTTP版本 状态码 说明
            2xx:代表成功
            3xx：代表重定向(某个服务器有问题会重定向到另外一台服务器上)
            4xx:代表浏览器故障
            5xx：代表服务器故障
    响应头：     
    Connection: Keep-Alive
        代表连接方式，keep-Alive:长连接
    Content-Encoding: gzip
        代表支持的压缩算法
    Content-Type: text/html; charset=utf-8
        代表返回浏览器请求的数据
    Date: Fri, 06 Apr 2018 11:42:46 GMT
        代表时间
        
        
    响应报文组成：
        响应行\r\n+响应头\r\n+空行(\r\n)+响应体(服务器发送给浏览器的数据)
'''


def main():
    # 创建tcpsocket套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(('www.baidu.com', 80))

    # 拼接请求报文
    # 请求行
    request_line = 'GET / HTTP/1.1\r\n'
    # 请求头
    request_headers = 'Host:www.baidu.com\r\n'
    # 报文数据
    request_data = request_line + request_headers + '\r\n'

    # 发送请求报文数据
    tcp_socket.send(request_data.encode('utf-8'))
    # 接收响应报文数据
    recv_data = tcp_socket.recv(10240)
    recv_data = recv_data.decode()
    # print(recv_data)
    # 解析响应报文数据
    # reslult = re.findall(r'\r\n\r\n(.*)', recv_data, re.S)
    reslult = recv_data.split('\r\n\r\n')[1]
    # reslult = reslult.decode()
    # 写入到文件中
    with open('info.txt', 'w') as file:
        file.write(reslult)

    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
