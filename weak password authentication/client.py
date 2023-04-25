import socket
import hashlib
import configparser


from salt import salt

config = configparser.ConfigParser()
config.read("config.ini")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6366))

choice_cfg = config['registration_of_a_nonexistent_name']['choice']
login_cfg = config['registration_of_a_nonexistent_name']['login']
password_cfg = config['registration_of_a_nonexistent_name']['password']


choice = choice_cfg
count = 0

run = True
while run:
    data = sock.recv(512)
    data.decode()
    choice = choice
    sock.send(choice.encode())
    print(data.decode())
    print(choice)

    if choice == '1':

        if count <= 0:
            login = login_cfg
            sock.send(login.encode())
            print('Login: ', login_cfg)
            print('password: ', password_cfg)
            data_sal = sock.recv(512)

            if data_sal == '':
                print(data_sal.decode())

            else:
                sal = bytearray(data_sal)
                hash_key = hashlib.pbkdf2_hmac('sha256', password_cfg.encode('utf-8'), sal, 100000).hex()
                #print('HASH: ', hash_key)
                sock.send(hash_key.encode())
            count += 1

    elif choice == '2':

        data = sock.recv(512)
        print(data.decode())

        if count <= 0:
            sol = salt()
            password = password_cfg
            sock.send(login_cfg.encode())
            hash_key = hashlib.pbkdf2_hmac('sha256', password_cfg.encode('utf-8'), sol, 100000).hex()
            print('Login: ', login_cfg)
            print('Password: ', password_cfg)
            #print('salt: ', sol)
            #print('HASH: ', hash_key)
            sock.send(hash_key.encode())
            sock.send(sol)