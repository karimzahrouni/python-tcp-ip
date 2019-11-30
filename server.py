import socket

host = '0.0.0.0'
port = 8855

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host,port))
serv.listen(5)

print("server create : ({},{})".format(host,port))

while True:
    conn, addr = serv.accept()
    from_client = ''
    print("client connect : ({},{})".format(addr[0],addr[1]))
    while True:
        data = conn.recv(4096)
        if not data: break
        print("server : "+data.decode())
        data = str(input("data from server to client transmitte: "))
        conn.send(str.encode(str(data)))

    conn.close()
    print('client disconnected')
