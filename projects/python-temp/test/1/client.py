import socket

HOST = '192.168.68.111'
PORT = 50007

for i in range(999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        commandInput = input("command: ")
        s.sendall(commandInput.encode())
        data = s.recv(1024)

    print('Server:', repr(data.decode('utf-8')))
# make some more changes