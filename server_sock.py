
import socket
import argparse

def pars_arg():
    parser = argparse.ArgumentParser(description="Client chat")
    parser.add_argument("--ip", dest="ip", required=True, help="ip server", type=str)
    parser.add_argument("--port", dest="port", required=True, help="port server", type=str)
    args = parser.parse_args()
    return args

def server_program():
    host = pars_arg().ip
    port = int(pars_arg().port)
    server_socket = socket.socket()  
    server_socket.bind((host, port)) 
    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        print("from connected user: " + str(data))
        data = input(" - SEND MESSAGE -> ")
        conn.send(data.encode()) 
    conn.close()  

if __name__ == '__main__':
    server_program()
