import socket
import time


# 71.206.101.118
# 192.168.1.13

HOST = "192.168.1.7"
PORT = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)
conn, addr = s.accept()
print("Connected by {0} on port {1}".format(*addr))

time.sleep(0.01)
conn.close()
