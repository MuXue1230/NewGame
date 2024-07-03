import pickle
import socket
import threading
from typing import Any

from cn.snowskystudio.newgame.test.Logger import Logger
from cn.snowskystudio.newgame.test.error.NetworkConnectionIndexOutOfRange import NetworkConnectionIndexOutOfRange
from cn.snowskystudio.newgame.test.error.NetworkConnectionSendDataFailed import NetworkConnectionSendDataFailed


class ServerNetworkController:
    HOST = 'localhost'
    PORT = 9008

    def __init__(self) -> None:
        self.listen_thread = None
        self.logger = Logger("ServerNetworkController")
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.logger.info("Server socket initialized.")
        self.listening = False
        self.clients = []

    def start(self) -> None:
        self.listening = True
        self.socket.bind((self.HOST, self.PORT))
        self.logger.info("Server socket bound (on %s %s)." % (self.HOST, self.PORT))
        self.socket.listen()
        self.logger.info("Server socket is listening (on %s %s)." % (self.HOST, self.PORT))
        self.listen_thread = threading.Thread(target=self.listener)
        self.listen_thread.start()

    def listener(self) -> None:
        while self.listening:
            try:
                conn, addr = self.socket.accept()
            except OSError:
                continue
            self.logger.info("Server socket accepted connection from %s %s." % (addr[0], addr[1]))
            self.clients.append(conn)

    def get_clients(self) -> list[socket.socket]:
        return self.clients

    def send(self, conn_id: int, data: Any) -> None:
        if conn_id < len(self.clients):
            self.clients[conn_id].sendall("SENDDATA".encode())
            check = self.clients[conn_id].recv(1024).decode()
            if check == "READY":
                self.clients[conn_id].sendall(pickle.dumps(data))
            else:
                raise NetworkConnectionSendDataFailed(
                    "Server socket failed to send data to %s." % self.clients[conn_id],
                    _from="cn.snowskystudio.newgame.network.ServerNetworkController - Line 47")
        else:
            raise NetworkConnectionIndexOutOfRange("The provided connection id (%d) is out of range." % conn_id,
                                                   _from="cn.snowskystudio.newgame.network.ServerNetworkController - "
                                                         "Line 43")

    def receive(self, conn_id: int) -> Any:
        if conn_id < len(self.clients):
            self.clients[conn_id].sendall("RECIVEDATA".encode())
            check = self.clients[conn_id].recv(1024).decode()
            if check == "READY":
                self.clients[conn_id].sendall("THEN".encode())
                data = self.clients[conn_id].recv(1024)
                return pickle.loads(data)
            else:
                raise NetworkConnectionSendDataFailed(
                    "Server socket failed to send data to %s." % self.clients[conn_id],
                    _from="cn.snowskystudio.newgame.network.ServerNetworkController - Line 62")
        else:
            raise NetworkConnectionIndexOutOfRange("The provided connection id (%d) is out of range." % conn_id,
                                                   _from="cn.snowskystudio.newgame.network.ServerNetworkController - "
                                                         "Line 43")

    def stop(self):
        self.logger.info("Server socket stopped.")
        self.listening = False
        for client in self.clients:
            client.close()
        self.socket.close()
