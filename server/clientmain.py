import socket
import time


HOST = "71.206.101.118"
PORT = 54321
BUFFSIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.close()

"""
while True:
    data = input("> ").encode()
    s.send(data)
    if data.decode() == "quit":
        print("closing")
        break
    time.sleep(.01)
    data = s.recv(4096).decode()
    print(data)

s.close()
"""