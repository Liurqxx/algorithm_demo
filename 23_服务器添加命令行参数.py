# _*_coding:utf-8_*_
# Author:liu
import socket
import gevent
from gevent import monkey
import sys

monkey.patch_all()


# webserver类
class WebServer(object):
    # 构造方法
    def __init__(self, port):
        # 初始化服务器基本配置
        # 创建服务器socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 端口复用
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定端口和ip
        self.server_socket.bind(("", port))
        # 变主动为被动套接字
        self.server_socket.listen(128)

    # 接收客户端的请求并处理
    def start_up(self):
        while True:
            # 监听客户端的连接
            client_socket, ip_port = self.server_socket.accept()
            # 开启协程处理请求
            gevent.spawn(self.request_handle, client_socket)

    # 处理请求逻辑
    def request_handle(self, client_socket):
        # 接收客户端的请求
        client_recv = client_socket.recv(4096)
        print('client_recv:', client_recv)

        # 获取请求资源路径
        request_url = WebServer.parse_http(client_recv.decode())

        # 拼接响应报文
        # 响应报文行
        response_line = 'HTTP/1.1 200 OK\r\n'
        # 响应报文头
        response_headers = 'MyServer\r\n'
        # 响应体
        with open('.' + request_url, 'rb') as file:
            response_body = file.read()

        # 响应报文
        response_data = (response_line + response_headers + '\r\n').encode('utf-8') + response_body

        # 发送响应报文
        client_socket.send(response_data)
        # 关闭连接
        client_socket.close()

    # 解析客户端请求得到请求资源地址
    @staticmethod
    def parse_http(request_data):
        # 获取请求行
        request_line = request_data.split('\r\n')[0]
        # 获取请求url
        request_url = request_line.split(' ')[1]

        return request_url


def main():
    # 命令行输入
    if len(sys.argv) < 2:
        print('你需要指定端口')
        return

    # if not isinstance(sys.argv[1], int):
    #     print('请输入整型数字')
    #     return
    # 获取端口
    port = int(sys.argv[1])

    # 初始化服务器
    web_server = WebServer(port)

    # 开启服务器
    web_server.start_up()


if __name__ == '__main__':
    main()
