# _*_coding:utf-8_*_
# Author:liu

import socket
import threading


# 接收消息
def recv_msg(client_socket):
    while True:
        recv_data = client_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('gbk')
            print('>>', recv_content)
        else:
            print('客户端断开连接了')
            client_socket.close()
            break


# 发送消息
def send_msg(client_socket):
    while True:
        send_data = input("<<:")
        send_content = send_data.encode('gbk')
        client_socket.send(send_content)


if __name__ == '__main__':
    # 创建tcpsocket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口和ip地址
    tcp_server_socket.bind(("", 8899))
    # 设置被动套接字
    tcp_server_socket.listen(128)
    while True:
        # 接收客户端连接请求
        client_socket, ip_port = tcp_server_socket.accept()
        # 创建线程处理客户端的请求
        client_thread_recv = threading.Thread(target=recv_msg, args=(client_socket,))
        client_thread_recv.setDaemon(True)
        client_thread_send = threading.Thread(target=send_msg, args=(client_socket,))
        client_thread_send.setDaemon(True)

        # 开启线程
        client_thread_recv.start()
        client_thread_send.start()
    # 服务端套接字关闭
    tcp_server_socket.close()
