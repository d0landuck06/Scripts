import socket
import time 
import pickle
HEADERSIZE = 10

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    #msg = "Welcome to the server"
    d = {1:'Yeet', 2: '!!!'}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg) : < {HEADERSIZE}}', "utf-8")+msg
    clientsocket.send(msg)

    
'''
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    msg = "Welcome to the server"
    msg = f'{len(msg) : < {HEADERSIZE}}'+msg
    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f'{len(msg) : < {HEADERSIZE}}'+msg
        clientsocket.send(bytes(msg, "utf-8"))
'''        