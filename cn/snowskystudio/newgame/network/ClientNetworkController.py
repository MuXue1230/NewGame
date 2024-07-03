import pickle
import socket
import threading
from typing import Any

from cn.snowskystudio.newgame.test.Logger import Logger


class ClientNetworkController:
    HOST = 'localhost'
    PORT = 9008

    def __init__(self) -> None:
        self.logger = Logger("ClientNetworkController")
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.logger.info("Client socket initialized.")
        self.connected = False
        self.data = {
            "send": [],
            "receive": []
        }
        self.handle_thread = None

    def connect(self) -> None:
        self.socket.connect((self.HOST, self.PORT))
        self.logger.info("Client connected to server (on %s %s)." % (self.HOST, self.PORT))
        self.connected = True
        self.handle_thread = threading.Thread(target=self.handle_data)
        self.handle_thread.start()

    def send(self, data: Any) -> None:
        self.data['send'].append(pickle.dumps(data))

    def receive(self) -> Any:
        if len(self.data['receive']) == 0:
            return None
        return self.data['receive'].pop(0)

    def disconnect(self) -> None:
        if self.connected:
            self.connected = False
            self.socket.close()
            self.logger.info("Client disconnected from server.")
        else:
            self.logger.error("Client socket is not connected.")

    def handle_data(self) -> None:
        send_data = False
        receive_data = False
        while self.connected:
            try:
                data = self.socket.recv(1024)
            except OSError:
                continue
            if send_data:
                self.data['receive'].append(pickle.loads(data))
                send_data = False
                continue
            elif receive_data:
                if len(self.data['send']) == 0:
                    self.socket.sendall(pickle.dumps(None))
                    receive_data = False
                    continue
                self.socket.sendall(self.data['send'].pop(0))
                receive_data = False
                continue
            elif data.decode() == 'SENDDATA':
                self.socket.sendall("READY".encode())
                send_data = True
                continue
            elif data.decode() == 'RECIVEDATA':
                self.socket.sendall("READY".encode())
                receive_data = True
                continue
