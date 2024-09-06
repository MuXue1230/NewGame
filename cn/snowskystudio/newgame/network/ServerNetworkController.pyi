from socket import socket
from threading import Thread
from typing import Any, Optional, Self

from cn.snowskystudio.newgame.test.Logger import Logger


class ServerNetworkController:
    HOST: str
    PORT: int
    
    logger: Logger
    
    socket: socket
    listen_thread: Optional[Thread]
    
    listening: bool
    clients: list[socket]
    
    def __init__(self) -> Self: ...
    
    def start(self) -> None: ...
    
    def listener(self) -> None: ...
    
    def get_clients(self) -> list[socket]: ...
    
    def send(self, conn_id: int, data: Any) -> None: ...
    
    def receive(self, conn_id: int) -> Any: ...
    
    def stop(self) -> None: ...
