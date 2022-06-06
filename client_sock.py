
import socket
import argparse

from click import argument

def pars_arg():
    parser = argparse.ArgumentParser(description="Client chat")
    parser.add_argument("--ip", dest="ip", required=True, help="ip server", type=str)
    parser.add_argument("--port", dest="port", required=True, help="port server", type=str)
    args = parser.parse_args()
    return args

def client_program():
    host = pars_arg().ip
    port = int(pars_arg().port)
    client_socket = socket.socket()  
    client_socket.connect((host, port))  
    print("send stoppp for stop connect")
    message = input(" - SEND MESSAGE -> ")  
    while message.lower().strip() != 'stoppp':
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode()  
        print('Received from server: ' + data)  
        message = input(" - SEND MESSAGE -> ") 
    client_socket.close()  

if __name__ == '__main__':
    client_program()