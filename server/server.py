import socket
import time


class Server (object):
    def __init__(self, buffSize=4096):
        self.buffSize = buffSize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ""
        self.port = 0

    def bind(self, host=socket.gethostbyname(socket.gethostname()), port=0):
        self.host = host
        self.port = port
        self.sock.bind((host, port))

    def runForever(self, backlog=5):
        self.sock.listen(backlog)

        client, addr = self.sock.accept()
        print("Connected by {0} on port {1}.".format(*addr))

        while True:
            try:
                data = self.sock.recv(self.buffSize)
                print(data.decode())
                print("> " + data)

                if data == "quit":
                    self.sock.close()
                    break

                self.sock.send("received".encode())
            except socket.error:
                print("Error receiving data.")
                break

        print("Closing.")
        time.sleep(0.01)
        self.sock.close()


s = Server()
s.bind(port=54321)
print("Host IP is", s.host)
s.runForever(5)



