import socket

sock = socket.socket()
# 绑定端口号和地址
sock.bind(("127.0.0.1",8800))
# 开启监听
sock.listen(5)

while 1:
    print("server waiting.....")
    # 测试 如如
    conn,addr = sock.accept()
    data = conn.recv(1024)
    print("data",data)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\nhello Pycharm")
    conn.close()