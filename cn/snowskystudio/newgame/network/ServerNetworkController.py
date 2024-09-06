import pickle
import socket
import threading

from cn.snowskystudio.newgame.test.Logger import Logger


class ServerNetworkController:
    HOST = 'localhost'
    PORT = 9008

    def __init__(self):
        self.listen_thread = None
        self.logger = Logger("ServerNetworkController")
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.logger.info("Server socket initialized.")
        self.listening = False
        self.clients = []

    def start(self):
        self.listening = True
        self.socket.bind((self.HOST, self.PORT))
        self.logger.info("Server socket bound (on %s %s)." % (self.HOST, self.PORT))
        self.socket.listen()
        self.logger.info("Server socket is listening (on %s %s)." % (self.HOST, self.PORT))
        self.listen_thread = threading.Thread(target=self.listener)
        self.listen_thread.start()

    def listener(self):
        while self.listening:
            try:
                conn, addr = self.socket.accept()
            except OSError:
                continue
            self.logger.info("Server socket accepted connection from %s %s." % (addr[0], addr[1]))
            self.clients.append(conn)

    def get_clients(self):
        return self.clients

    def send(self, conn_id, data):
        self.clients[conn_id].sendall("SENDDATA".encode())
        self.clients[conn_id].recv(1024).decode()
        self.clients[conn_id].sendall(pickle.dumps(data))

    def receive(self, conn_id):
        self.clients[conn_id].sendall("RECIVEDATA".encode())
        self.clients[conn_id].recv(1024).decode()
        self.clients[conn_id].sendall("THEN".encode())
        data = self.clients[conn_id].recv(1024)
        return pickle.loads(data)

    def stop(self):
        self.logger.info("Server socket stopped.")
        self.listening = False
        for client in self.clients:
            client.close()
        self.socket.close()
