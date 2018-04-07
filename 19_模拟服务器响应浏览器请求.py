# _*_coding:utf-8_*_
# Author:liu
import socket


# 客户端处理
def handle(client_socket):
    # 接收请求报文
    client_data = client_socket.recv(4096)

    if not client_data:
        # 客户端断开连接
        print("客户端断开连接了。。。")
        client_socket.close()
        return
    print(client_data.decode())

    # 拼接响应报文
    # 响应行
    response_line = 'HTTP/1.1 200 请求成功\r\n'
    # 响应头
    response_headers = 'MyServer\r\n'
    # 响应体
    response_content = 'welcome you!!!\r\n'
    # 响应报文
    response_data = response_line + response_headers + '\r\n' + response_content

    # 发送响应报文
    client_socket.send(response_data.encode('utf-8'))

    # 关闭套接字
    client_socket.close()


if __name__ == '__main__':
    # 创建服务端socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定端口和ip信息
    server_socket.bind(("", 8899))

    # 变主动为被动套接字
    server_socket.listen(128)

    while True:
        # 监听客户端的连接
        client_socket, ip_port = server_socket.accept()

        # 处理客户端的请求
        handle(client_socket)

    # 关闭服务端套接字
    server_socket.close()
