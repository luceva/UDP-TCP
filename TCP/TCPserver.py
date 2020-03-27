'''
Name: Ante Lucev
Date: 3-26-2020
Desc: server.py for client/server chat room
'''
import socket
import threading
import pickle

def TCPworker(sockets):
    client_socket,addr,name = sockets[-1]
    print(addr)
    print("There are {} things in socket_list.".format(len(sockets)))
    while True:
        try:
            msg = client_socket.recv(1024)
        except ConnectionResetError:
            sockets.remove((client_socket, addr, name))
            names_on = []
            for other_soc, other_addr, other_name in sockets:
                names_on.append(other_name)
            message = pickle.dumps(("On are:",names_on))
            for other_soc, other_addr, other_name in sockets:
                other_soc.sendall(message)
            print("Client disconnect")
            break
        msg = pickle.loads(msg)
        for other_soc, other_addr, other_name in sockets:
            if (client_socket,addr,name) != (other_soc, other_addr, other_name):
                message = pickle.dumps((name, msg))
                other_soc.sendall(message)
            else:
                message = pickle.dumps(("You", msg))
                client_socket.sendall(message)

port = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_list = []

s.bind( ('127.0.0.1', port) )
s.listen()

while True:
    print("Waiting for accept")
    client_socket, addr = s.accept()
    name = client_socket.recv(1024)
    name = name.decode('ascii')
    socket_list.append( (client_socket,addr,name) )
    names_on = []
    for other_soc, other_addr, other_name in socket_list:
        names_on.append(other_name)
    message = pickle.dumps(("On are:", names_on))
    for other_soc, other_addr, other_name in socket_list:
        other_soc.sendall(message)
    thread = threading.Thread(target=TCPworker, args= [socket_list] )
    thread.start()