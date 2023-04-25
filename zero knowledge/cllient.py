import socket
import sympy
import random

class connection():
    def __init__(self):
        self.ip_addres = 'localhost'
        self.port = 6666
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conn_server(self):
        server_address = ('localhost', 6666)
        self.client_socket.connect(server_address)

    def send(self, msg):
        self.client_socket.send(str(msg).encode())

    def take(self):
        message = int(self.client_socket.recv(2048).decode())
        return message

    def take_str(self):
        message = self.client_socket.recv(64).decode()
        return message

class verification():
    def __init__(self):
        self.counter = 1
        self.rounds = 21
        self.n = None
        self.secret = None
        self.v =None
        self.rand_r = None
        self.x = None
        self.bit_e = None
        self.y = None

    def createV(self):
        self.secret = sympy.randprime(1, self.n - 1)
        self.v = self.secret ** 2 % self.n
        return self.v

    def random_r(self):
        self.rand_r = random.randint(1, self.n - 1)
        return self.rand_r

    def RX(self):
        self.x = self.rand_r ** 2 % self.n
        return self.x

    def createY(self):
        if self.bit_e == 0:
            self.y = self.rand_r
            return self.y
        else:
            self.y = self.rand_r * self.secret ** self.bit_e % self.n
            return self.y




ver = verification()
conn = connection()
conn.conn_server()
ver.n = conn.take()
ver.v = ver.createV()
conn.send(ver.v)
while ver.counter != ver.rounds:
    ver.rand_r = ver.random_r()
    ver.x = ver.RX()
    conn.send(ver.x)
    ver.bit_e = conn.take()
    ver.y = ver.createY()
    conn.send(ver.y)
    print(f"Round #{ver.counter} >>> " + conn.take_str())
    ver.counter += 1