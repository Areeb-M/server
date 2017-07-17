import socket
import time


HOST = ""
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)
conn, addr = s.accept()
print("Connected by {0} on port {1}".format(*addr))

while True:
    data = conn.recv(4096).decode()
    print(">", data)
    if data == "quit":
        print("Closing")
        break
    print("a")
    conn.send("a".encode())

time.sleep(0.01)
conn.close()

