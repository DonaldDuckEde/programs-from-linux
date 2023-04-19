import socket
import threading

HOST = '192.168.68.111'
PORT = 50007

def handle_client(conn, addr):
    print('Request by', addr)
    while True:
        rawData = conn.recv(1024)
        if not rawData:
            break
        
    data = rawData.decode('utf-8')
    
    if data == "quit":
        conn.close()

    conn.sendall(data)
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr))
            t.start()

if __name__ == '__main__':
    start_server()
