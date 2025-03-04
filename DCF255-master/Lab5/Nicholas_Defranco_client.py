// code taken from https://youtu.be/XiVVYfgDolU 

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ").encode();
    while message != 'q':
        s.send(message);
        data = s.recv(1024)
        print('Received from server: ' + str(data))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
