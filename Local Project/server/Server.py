import socket
    
class App:
    def __init__(ip='192.168.137.45', port = 8000):
        self.IP = ip
        self.PORT = port

    def getAll():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.137.45', self.PORT))
        sock.send(b"GET_ALL")

        response = sock.recv(4096)
        sock.close()
        print(response)
        print(response.decode())
        
        return response.decode()

    
    def add(esp32IP= "192.168.137.125"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.IP, self.PORT))
        sock.send(b"ADD"+esp32IP)
        response = sock.recv(4096)
        sock.close()
        


