import hashlib
import random
import socket

class connection():
    def __init__(self):
        self.ip_addres = 'localhost'
        self.port = 6666
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conn_server(self):
        server_address = ((self.ip_addres, self.port))
        self.client_socket.connect(server_address)

    def send(self, msg):
        self.client_socket.send(str(msg).encode())

    def take(self):
        message = int(self.client_socket.recv(1024).decode())
        return message

    def take_str(self):
        message = self.client_socket.recv(64).decode()
        return message

class Encryption():
    def __init__(self):
        self.N_times = 100000
        self.counter_ident = 2
        self.password = None
        self.login = None
        self.A = None
        self.old_A = 0
        self.hashed = None
        self.na_times = None
        self.cnt = 1


    def hash_password(self, password, login):
        password_bytes = password.encode('utf-8')
        servername_bytes = login.encode('utf-8')
        hash_obj = hashlib.sha256(password_bytes + servername_bytes)
        p_hex = hash_obj.hexdigest()
        p = int(p_hex, 16)
        return p

    def hash_n_times(self, p, n):
        p_bytes = p.to_bytes((p.bit_length() + 7) // 8, byteorder='big')
        for i in range(n):
            hash_obj = hashlib.sha256(p_bytes)
            p_bytes = hash_obj.digest()
            p_n = int.from_bytes(p_bytes, byteorder='big')
        return p_n

class registr(Encryption):
    def __init__(self):
        self.login = '123'
        self.password = '123'
        self.N = 100000
        self.acc = None


reg = registr()
p = reg.hash_password(reg.password, reg.login)
reg.acc = reg.hash_n_times(p, reg.N)

conn = connection()
conn.conn_server()
conn.send(reg.acc)
enc = Encryption()

while True:
    if enc.cnt <= enc.counter_ident:
        enc.old_A = enc.A
        enc.A = conn.take()
        enc.login = input('Enter password >>> ')
        enc.password = input('Enter login >>> ')
        enc.hashed = enc.hash_password(enc.login, enc.password)
        if enc.old_A != enc.A:
            enc.na_times = enc.N_times - enc.A
            enc.hashed = enc.hash_n_times(enc.hashed, enc.na_times)
            conn.send(enc.hashed)
            print(f"Sessin #{enc.cnt} >>> " + conn.take_str())
            enc.cnt +=1
    else:
        print('Number of attempts completed')
        break

