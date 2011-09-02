import re
import socket

class util_exception(Exception):
    pass

class Abstract():
    __host = None
    __port = None
    __timeout = 30
    __proto = 'tcp'
    __sock = None
    
    def __init__(self, host, port, timeout=30, proto='tcp'):
        self.__sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        self.__proto = proto
        self.__sock.settimeout(timeout)
    
    def __connect__(self):
        if self.__sock:
            self.__sock.connect(self.__host, self.__port)
    
    def __disconnect__(self):
        try:
            self.__sock.close()
            self.__sock = None
        except Exception:
            pass

class Smtp(Abstract):
    
    __banner = None
    
    def __init__(self, host, port=25):
        Abstract.__init__(self, host, port)
        
    def getBanner(self):
        try: 
            self.__connect__()
            self.__banner = self.__sock.recv(4096)
            self.__disconnect__()
            return self.__banner
        except Exception:
            return None
        
        