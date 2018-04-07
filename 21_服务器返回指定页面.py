# _*_coding:utf-8_*_
# Author:liu

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SOL_SOCKET
from socket import SO_REUSEADDR

'''
my_http: {'Connection': 'keep-alive', 'Host': '192.168.107.87', 
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
 'Upgrade-Insecure-Requests': '1', 'method': 'GET', 'version': 'HTTP/1.1', 'Accept-Encoding': 'gzip, deflate', 
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'url': '/index.html', 
 'Accept-Language': 'zh-CN,zh;q=0.9'}

'''


def parse_http(request_data):
    my_http = {}

    # 分成多行
    request_headers = request_data.split('\r\n')
    # 分割请求行
    request_lines = request_headers[0].split(' ')
    # 拼接请求行
    my_http['method'] = request_lines[0]
    my_http['url'] = request_lines[1]
    my_http['version'] = request_lines[2]

    # 获取请求头信息
    for header in request_headers[1:]:

        if not header:
            continue
        # 分割然后拼接请求头信息
        lines = header.split(':')
        my_http[lines[0]] = lines[1][1:]
    print('my_http:', my_http)
    return my_http


def request_handler(sock):
    """处理客户端请求"""

    request_data = sock.recv(4096)
    if not request_data:
        print('客户端已经断开连接.')
        sock.close()
        return

    # 解析 HTTP 文本
    my_http = parse_http(request_data.decode('utf-8'))

    # 读取固定页面数据
    try:
        response_line = 'HTTP/1.1 200 OK\r\n'
        response_header = 'Server: PythonWebServer1.0\r\n'
        file = open('./' + my_http['url'], 'rb')
    except:
        response_line = 'HTTP/1.1 404 NOT FOUND\r\n'
        response_header = 'Server: PythonWebServer1.0\r\n'
        file = open('./404.html', 'rb')

    # 读取文件内容
    response_content = file.read()
    # 拼接响应报文
    response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_content
    # 发送响应报文
    sock.send(response_data)
    # 关闭套接字
    sock.close()


def main():
    # 创建套接字
    sock = socket(AF_INET, SOCK_STREAM)
    # 设置套接字复用地址
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定IP地址和端口
    sock.bind(('', 8899))
    # 设置被动套接字
    sock.listen(128)

    while True:
        # 等待被连接
        client_sock, client_addr = sock.accept()
        # 处理请求
        request_handler(client_sock)


if __name__ == '__main__':
    main()
