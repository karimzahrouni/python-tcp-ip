import socket

host = '0.0.0.0'
port = 8855
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port ))


while(1) : 
    data = str(input("ur data client to transmite :"))
    client.send(str.encode(data))
    dataRecu = client.recv(4096)
    print("ur data : "+dataRecu.decode())

client.close()
