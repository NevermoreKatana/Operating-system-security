import socket
import random
import sympy
import time
import math
from bbs import bit_e

class connection():
    def __init__(self):
        self.ip_addres = 'localhost'
        self.port = 6666
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_addres = None

    def open_server(self):
        self.server_socket.bind((self.ip_addres, self.port))
        self.server_socket.listen(1)
        self.client_socket, self.client_addres = self.server_socket.accept()
        print(f"Подключился {self.client_addres}")

    def send(self, msg):
        self.client_socket.send(str(msg).encode())

    def take(self):
        message = int(self.client_socket.recv(2048).decode())
        return message

class prime():
    def __init__(self):
        self.p = None
        self.q = None
        self.n = None
        self.x = None
        self.v = None
        self.y = None
        self.bit_e = None
        self.stop = False

    def prime_number(self):
        self.p = sympy.randprime(2 ** 1023, 2 ** 1024 - 1)
        self.q = sympy.randprime(2 ** 1023, 2 ** 1024 - 1)
        self.n = self.p * self.q
        return self.n

    def createE(self):
        self.bit_e = int(bit_e.generate_e())
        return self.bit_e

    def verification(self):
        verific = self.x * self.v ** self.bit_e % self.n
        if self.y ** 2 % self.n == verific:
            msg = 'Accept'
        else:
            msg = "Fail"
        return msg


conn = connection()
conn.open_server()
numb = prime()
N = numb.prime_number()
conn.send(N)
numb.v = conn.take()
conter = 1
while numb.stop == False:
    numb.x = conn.take()
    numb.bit_e = 1
    conn.send(numb.bit_e)
    numb.y = conn.take()
    conn.send(numb.verification())
    if numb.verification() == 'Fail':
        numb.stop = True





