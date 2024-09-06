from socket import socket
from threading import Thread
from typing import Any, Optional, Self

from cn.snowskystudio.newgame.test.Logger import Logger


class ClientNetworkController:
    HOST: str
    PORT: int
    
    logger: Logger
    
    socket: socket
    handle_thread: Optional[Thread]
    connected: bool

    data: dict[str, list[Any]]
    
    def __init__(self) -> Self: ...
    
    def connect(self, host: Optional[str]=None, port: Optional[int]=None) -> None: ...
    
    def send(self, data: Any) -> None: ...
    
    def receive(self) -> Any: ...
    
    def disconnect(self) -> None: ...
    
    def handle_data(self) -> None: ...
