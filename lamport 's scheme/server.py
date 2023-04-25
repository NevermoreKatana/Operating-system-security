import hashlib
import socket

class connection():
    def __init__(self):
        self.ip_addres = 'localhost'
        self.port = 6666
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_addres = None
        self.client_socket = None

    def open_server(self):
        self.server_socket.bind((self.ip_addres, self.port))
        self.server_socket.listen(1)
        self.client_socket, self.client_addres = self.server_socket.accept()
        print(f"Подключился >>>> {self.client_addres}")

    def send(self, msg):
        self.client_socket.send(str(msg).encode())

    def take(self):
        message = int(self.client_socket.recv(1024).decode())
        return message

class verification():
    def __init__(self):
        self.reg_acc = None
        self.N_times = 100000
        self.A = 1
        self.old_A = None
        self.hashed = None

    def hash_n_times(self, p, n):
        p_bytes = p.to_bytes((p.bit_length() + 7) // 8, byteorder='big')
        for i in range(n):
            hash_obj = hashlib.sha256(p_bytes)
            p_bytes = hash_obj.digest()
        return int.from_bytes(p_bytes, byteorder='big')


conn = connection()
conn.open_server()
ver = verification()
ver.reg_acc = conn.take()

while True:
    if ver.old_A != ver.A:
        ver.old_A = ver.A
        conn.send(ver.A)
        ver.hashed = conn.take()
        ver.hashed = ver.hash_n_times(ver.hashed, ver.A)
        if ver.hashed == ver.reg_acc:
            msg = 'Accepted'
            conn.send(msg)
            ver.A +=1
        else:
            msg = 'Failed'
            conn.send(msg)
            ver.A +=1
