import sympy
import socket
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)


class Connection_control():
    def __init__(self):
        self.ip_addres = 'localhost'
        self.port = 6666
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        server_address = (self.ip_addres, self.port)
        self.client_socket.connect(server_address)

    def send(self, msg):
        self.client_socket.send(str(msg).encode())
        print(Fore.BLUE + f"Sent >>>> {msg} <<<< to" + Fore.RED + f" {self.ip_addres}:{self.port}")
        return None

    def take(self):
        message = int(self.client_socket.recv(2048).decode())
        print(Fore.CYAN + f"Receive >>>> {message} <<<< from" + Fore.RED + f" {self.ip_addres}:{self.port}")
        return message

    def take_str(self):
        message = self.client_socket.recv(2048).decode()
        print(Fore.CYAN + f"Receive >>>> {message} <<<< from" + Fore.RED + f" {self.ip_addres}:{self.port}")
        return message


class Generate_key():
    def secret_key(self):
        secret_key = sympy.randprime(2**15, 2**16-1)
        print(Fore.MAGENTA + f'Generated a secret key >>>> {secret_key}')
        return secret_key

    def open_key(self, n):
        open_key = sympy.randprime(1, n)
        print(Fore.MAGENTA + f'Generated a public key >>>> {open_key}')
        return open_key


class keys_operator():
    def __init__(self):
        self.public_key = None
        self.public_key1 = None
        self.secret_key = None
        self.part_key = None
        self.full_key = None

    def create_part_key(self):
        part_key = self.public_key ** self.secret_key % self.public_key1
        print(Fore.MAGENTA + f'Generated a partial key >>>> {part_key}')
        return part_key

    def create_full_key(self):
        self.full_key = self.part_key ** self.secret_key % self.public_key1
        print(Fore.MAGENTA + f'Generated full key >>>> {self.full_key}')
        return self.full_key


class enc_deci():
    def __init__(self):
        self.encrypted_message = ""
        self.decipher_message = ""
        self.message = 'Always think about cybersecurity, Diffie-Hellman key exchange protocol'

    def encrypt(self, key):
        for symbol in self.message:
            self.encrypted_message += chr(ord(symbol) + key)
        print(Fore.YELLOW + f'Encrypted this message >>>> {self.message}')
        return self.encrypted_message

    def decipher(self, key):
        self.message = ""
        print(Fore.LIGHTCYAN_EX + f"Deciphering this message >>>> {self.decipher_message}")
        for symbol in self.decipher_message:
            self.message += chr(ord(symbol) - key)
        print(f"Decrypted message >>>> {self.message}")
        return self.message


gen = Generate_key()
A_part = keys_operator()
conn = Connection_control()
conn.connect()
enc_dec = enc_deci()

if __name__ == "__main__":
    secret_key = gen.secret_key()
    public_key = gen.open_key(secret_key)
    conn.send(public_key)
    public_key_B = conn.take()
    A_part.public_key = public_key
    A_part.public_key1 = public_key_B
    A_part.secret_key = secret_key
    part_key_A = A_part.create_part_key()
    conn.send(part_key_A)
    part_key_B = conn.take()
    A_part.part_key = part_key_B
    full_key = A_part.create_full_key()
    enc_dec.encrypt(A_part.full_key)
    conn.send(enc_dec.encrypted_message)
    enc_dec.decipher_message = conn.take_str()
    enc_dec.decipher(A_part.full_key)