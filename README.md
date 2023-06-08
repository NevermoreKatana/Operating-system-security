# Безопасность операционных систем
<a href="https://codeclimate.com/github/NevermoreKatana/Operating-system-security/maintainability"><img src="https://api.codeclimate.com/v1/badges/c4a6dc8125d033de2747/maintainability" /></a>
## Описание
Этот проект содержит реализации различных методов обеспечения безопасности операционных систем.

```sh
Автоматическая установка виртуального окружения и всех библиотек описаны в Readme.md файлах в папках!
```

# Генератор псевдослучайных битовых последовательностей
Содержит реализацию генератора псевдослучайных битовых последовательностей для операционных систем. Этот генератор может использоваться для генерации ключей шифрования, паролей и других случайных значений в системе.

# Реализация слабой парольной аутентификации внутри клиент-серверного приложения:
Содержит реализацию метода слабой парольной аутентификации внутри клиент-серверного приложения. Этот метод может использоваться для обеспечения базовой защиты в системах, где сложная аутентификация не требуется.

# Реализация аутентификации внутри клинет-серверного приложения по схеме лэмпорта: 
Содержит реализацию аутентификации внутри клиент-серверного приложения по схеме лэмпорта. Этот метод может использоваться для обеспечения более высокой защиты в системах, где требуется более сложная аутентификация.

# Реализация внутри клиент-серверного приложения аутентификации с нулевым разглашением: 
Содержит реализацию метода аутентификации с нулевым разглашением внутри клиент-серверного приложения. Этот метод может использоваться для обеспечения более высокой защиты в системах, где требуется полная конфиденциальность аутентификационных данных.

# Реализация в клиент-серверном приложении протокола Диффи-Хеллмана:
Содержит реализацию протокола Диффи-Хеллмана в клиент-серверном приложении. Этот метод может использоваться для обеспечения безопасного обмена ключами между клиентом и сервером.

# Реализация эмулятора дискреционной модели Харрисона-Руззо-Ульмана: 
Содержит реализацию эмулятора дискреционной модели Харрисона-Руззо-Ульмана для операционных систем. Дискреционная модель Харрисона-Руззо-Ульмана является одним из методов контроля доступа в операционных системах, который позволяет ограничить права доступа пользователя к ресурсам на основе политик безопасности и установленных правил. Этот эмулятор позволяет пользователям понять, как работает дискреционная модель Харрисона-Руззо-Ульмана и как можно управлять правами доступа для обеспечения безопасности системы.

# Реализация эмулятора дискреционной модели Тейк-Грант: 
Модель "Тейк-Грант" (Take-Grant) является формальной моделью для анализа безопасности и контроля доступа в компьютерных системах. Она была разработана в 1970-х годах Джеральдом Петти и Карлом Харрисом, и с тех пор получила широкое применение в области информационной безопасности.

Основная идея модели Тейк-Грант заключается в представлении системы в виде графа, где субъекты (пользователи) и объекты (ресурсы) представлены узлами, а связи между ними представляют собой разрешенные или запрещенные права доступа. Эти связи представляют собой операции "взять" (take) и "предоставить" (grant). Операция "взять" позволяет субъекту получить доступ к объекту, а операция "предоставить" позволяет субъекту предоставить доступ другому субъекту к объекту.

# Реализация эмулятора дискреционной модели Белла-Лападулла: 
Модель Белла-Лападулла - это модель безопасности и контроля доступа, используемая для защиты конфиденциальности и целостности информации в компьютерных системах. Названная в честь исследователей Денниса Белла и Роджера Лападуллы, эта модель была представлена в 1973 году и стала одним из основных вкладов в область информационной безопасности.

Основная идея модели Белла-Лападулла заключается в принципе "неизлишне права доступа" (principle of least privilege) и обязательном контроле доступа (mandatory access control). Согласно этой модели, каждый субъект (пользователь или процесс) и объект (файлы, базы данных и т.д.) в системе имеют определенный уровень секретности и важности, выраженный в виде меток безопасности.

# Реализация эмулятора дискреционной ролевой модели(RBAC):
Ролевая модель, также известная как RBAC (Role-Based Access Control), является одним из методов контроля доступа в информационных системах. В этой модели доступ к ресурсам системы предоставляется на основе ролей, которые назначаются пользователям.

# P.s. Весь код сделан в обучающих целях
Я не являюсь профессиональным разработчиком, данные программы сделаны в целях обучения, я никого не призываю использовать данный код как проффесиональный.

# Operating system security

## Description
This project contains implementations of various methods to ensure the security of operating systems.


# Pseudorandom bit sequence generator
Contains an implementation of a pseudorandom bit sequence generator for operating systems. This generator can be used to generate encryption keys, passwords, and other random values in the system.

# Implementation of weak password authentication inside a client-server application:
Contains an implementation of a weak password authentication method inside a client-server application. This method can be used to provide basic protection in systems where complex authentication is not required.

# Implementation of authentication inside a wedge server application according to the lamport scheme: 
Contains the implementation of authentication inside the client-server application according to the lamport scheme. This method can be used to provide higher security in systems where more complex authentication is required.

# Implementation of zero-knowledge authentication inside a client-server application: 
Contains an implementation of a zero-knowledge authentication method inside a client-server application. This method can be used to provide higher protection in systems where complete confidentiality of authentication data is required.

# Implementation of the Diffie-Hellman protocol in a client-server application:
Contains the implementation of the Diffie-Hellman protocol in a client-server application. This method can be used to ensure secure key exchange between the client and the server.

# Implementation of the Harrison-Ruzzo-Ullman discretionary model emulator: 
Contains an implementation of the Harrison-Ruzzo-Ullman discretionary model emulator for operating systems. The Harrison-Ruzzo-Ullman discretionary model is one of the access control methods in operating systems that allows you to restrict user access rights to resources based on security policies and established rules. This emulator allows users to understand how the Harrison-Ruzzo-Ullman discretionary model works and how access rights can be managed to ensure system security.

# Implementation of the discretionary Take-Grant model emulator:
The Take-Grant model is a formal model for security analysis and access control in computer systems. It was developed in the 1970s by Gerald Petty and Carl Harris, and has since been widely used in the field of information security.

The main idea of the Take-Grant model is to represent the system in the form of a graph, where subjects (users) and objects (resources) are represented by nodes, and the connections between them represent permitted or prohibited access rights. These relationships are operations "take" (take) and "grant" (grant). The "take" operation allows a subject to gain access to an object, and the "grant" operation allows a subject to grant access to another subject to an object.

# Implementation of the Bell-Lapadulla discretionary model emulator: 
The Bella-Lapadulla model is a security and access control model used to protect the confidentiality and integrity of information in computer systems. Named after researchers Dennis Bell and Roger Lapadulla, this model was introduced in 1973 and has become one of the main contributions to the field of information security.

The main idea of the Bella-Lapadulla model is the principle of "non-exclusive access rights" (principle of least privilege) and mandatory access control (mandatory access control). According to this model, each subject (user or process) and object (files, databases, etc.) in the system have a certain level of secrecy and importance, expressed in the form of security labels.

# Implementation of the Discretionary Role Model Emulator (RBAC):
The role model, also known as RBAC (Role-Based Access Control), is one of the access control methods in information systems. In this model, access to system resources is provided based on the roles that are assigned to users.

# P.s. All the code is made for educational purposes
I am not a professional developer, these programs are made for training purposes, I do not encourage anyone to use this code as professional.
