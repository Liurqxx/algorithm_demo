# _*_coding:utf-8_*_
# Author:liu
import socket
import re

'''
请求报文:
    请求行：
    GET / HTTP/1.1
    请求行格式：
      请求方式 请求的资源路径 HTTP版本

    请求头：
    Host: www.baidu.com
        代表被浏览器请求的服务器地址(端口)
    Connection: keep-alive
        代表连接方式 keep-alive-->长连接
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36
        代表浏览器的访问服务器的身份信息
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        代表浏览器可以接收的文件类型
    Accept-Encoding: gzip, deflate, br
        代表浏览器可接受的压缩算法
    Accept-Language: zh-CN,zh;q=0.9
        代表浏览器支持的语言

    请求报文组成：
        请求行\r\n+请求头\r\n+空行(\r\n)+请求体\r\n(浏览器给服务器发送的数据,GET没有数据)


'''


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
