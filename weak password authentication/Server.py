import socket
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, name_db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=name_db
        )
        print("Подключение к базе данных успешно ")
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    return connection


connect = create_connection("localhost", "php", "159357456KA", "bos")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 6366))
sock.listen(10)


while True:
    connection, addr = sock.accept()
    print("Connected by ", addr)
    connection.send('Выберите тип: \n1-Вход\n2-Регистрация'.encode())
    choice = connection.recv(4)
    cur = connect.cursor()
    cur.execute("SELECT Id FROM `account`")
    result = cur.fetchall()
    if result == []:
        x = 0
    else:
        x = result[0][0] + 1
    if choice.decode() == '1':
        print('Получен тип вход')
        login = connection.recv(16)
        login = login.decode()
        cur = connect.cursor()
        cur.execute(f"SELECT * FROM `account` WHERE `UserName` LIKE '{login}'")
        result1 = cur.fetchall()
        if result1 == []:
            connection.send('Невеный логин или пароль'.encode())
        else:
            res = result1[0][3]
            sll = connection.sendall(res.encode())
            hash_key = connection.recv(256)
            hash_key = hash_key.decode()
            cur = connect.cursor()
            print('Login: ', login, '\nHashkey: ', hash_key)
            cur.execute(f"SELECT `Id`, `UserName`, `Hash` FROM `account` "
                    f"WHERE `UserName` = '{login}'")
            result = cur.fetchall()
            if result == []:
                connection.send('Неверный логин или пароль'.encode())
            else:
                login_bd = result[0][1]
                hash_bd = result[0][2]
                if login_bd == login and hash_key == hash_bd:
                    connection.send('Аутентификация пройдена'.encode())
                else:
                    connection.send('Аутентификация не пройдена\nНеверный логин или пароль'.encode())
    elif choice.decode() == '2':
        connection.send('Введите login\nВведеите пароль'.encode())
        print('Получен тип регистрация ')
        login = connection.recv(16)
        login = login.decode()
        hash_key = connection.recv(256)
        hash_key = hash_key.decode()
        sal = connection.recv(256)
        sal = sal.decode()
        print('Login: ', login, '\nHash key: ', hash_key, '\nSalt: ', sal)
        cur = connect.cursor()
        cur.execute(f"SELECT `UserName`FROM `account` "
                    f"WHERE UserName = '{login}'")
        result = cur.fetchall()
        try:
            insert_new_account = "INSERT INTO `account`(`Id`, `UserName`, `Hash`, `Salt`) " \
                                 f"VALUES ('{x}','{login}','{hash_key}', '{sal}')"
            with connect.cursor() as cursor:
                cursor.execute(insert_new_account)
                connect.commit()
                connection.send('Данные успешно получены\nДоступ в сессию получен'
                                '\nЧтобы пользоваться возможностями, переподключитесь'.encode())
        except:
            connection.send('Такой пользователь уже существует'.encode())
