# _*_coding:utf-8_*_
# Author:liu
import socket

if __name__ == '__main__':
    # 创建tcpsocket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    tcp_socket.connect(("www.baidu.com", 80))

    # 拼接请求报文
    # 请求行
    request_line = 'GET / HTTP/1.1\r\n'
    # 请求头
    request_headers = 'Host:www.baidu.com\r\n'
    # 请求报文
    request_data = request_line + request_headers + '\r\n'

    # 发送请求报文
    tcp_socket.send(request_data.encode('utf-8'))

    # 接收响应报文
    recv_data = tcp_socket.recv(4096)
    recv_data = recv_data.decode()

    # 解析响应报文数据
    recv_info = recv_data.split('\r\n\r\n')[1]

    print(recv_info)

    # 关闭套接字
    tcp_socket.close()
