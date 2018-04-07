# _*_coding:utf-8_*_
# Author:liu

import socket


# 处理客户端的请求
def handle(client_socket):
    # 接收客户端请求报文
    recv_data = client_sockewt.recv(4096)
    # 客户端断开连接
    if not recv_data:
        print("客户端断开连接")
        client_sockewt.close()
        return

    print(recv_data.decode())

    # 拼接响应报文
    # 响应行
    response_line = 'HTTP/1.1 200 成功\r\n'
    # 响应头
    response_headers = 'MyServer\r\n'
    # 响应体
    with open('index.html', 'rb') as file:
        response_body = file.read()
    # 响应报文
    response_data = (response_line + response_headers + '\r\n').encode('utf-8') + response_body

    # 发送响应报文
    client_sockewt.send(response_data)

    # 关闭套接字
    client_sockewt.close()


if __name__ == '__main__':
    # 创建服务端socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定ip和端口
    server_socket.bind(("", 8899))

    # 变主动为被动
    server_socket.listen(128)

    while True:
        # 监听客户端的连接
        client_sockewt, ip_port = server_socket.accept()
        handle(client_sockewt)

    # 关闭服务端套接字
    server_socket.close()
