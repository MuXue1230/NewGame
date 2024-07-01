import pickle
import socket
import threading
from typing import Any

from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.test.Logger import Logger


class ClientNetworkController:
    HOST = '::1'
    PORT = 32768

    def __init__(self) -> None:
        self.logger = Logger("ClientNetworkController")
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.logger.info("Client socket initialized.")
        self.connected = False
        self.datas = {
            "send": [],
            "receive": []
        }
    
    def connect(self) -> None:
        self.socket.connect((self.HOST, self.PORT))
        self.logger.info("Client connected to server (on %s %s)." %(self.HOST, self.PORT))
        self.connected = True
        self.handle_thread = threading.Thread(target=self.handle_data)
        self.handle_thread.start()
    
    def send(self, data: Any) -> None:
        self.datas['send'].append(pickle.dumps(data))
    
    def receive(self) -> Any:
        if len(self.datas['receive']) == 0: return None
        return self.datas['receive'].pop(0)
    
    def disconnect(self) -> None:
        if self.connected:
            self.connected = False
            self.socket.close()
            self.logger.info("Client disconnected from server.")
        else:
            self.logger.error("Client socket is not connected.")
    
    def handle_data(self) -> None:
        senddata = False
        recivedata = False
        while self.connected:
            try: data = self.socket.recv(1024)
            except OSError: continue
            if senddata:
                self.datas['receive'].append(pickle.loads(data))
                senddata = False
                continue
            elif recivedata:
                if len(self.datas['send']) == 0:
                    self.socket.sendall(pickle.dumps(None))
                    recivedata = False
                    continue
                self.socket.sendall(self.datas['send'].pop(0))
                recivedata = False
                continue
            elif data.decode() == 'SENDDATA':
                self.socket.sendall("READY".encode())
                senddata = True
                continue
            elif data.decode() == 'RECIVEDATA':
                self.socket.sendall("READY".encode())
                recivedata = True
                continue
