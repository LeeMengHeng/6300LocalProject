import socket
import datetime
import json
import re

class Server:
    # address = '192.168.137.39'
    def __init__(self, esp32Dict = {"192.168.137.142": 0}, ip='192.168.137.45', port = 8000):
        #self.password = password
        #self.address = address
        self.ip = ip
        self.port = port
        self.esp32Dict = esp32Dict
    
    def start(self):
        # 建立一个服务端
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 以下设置解决ctrl+c退出后端口号占用问题
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        server.bind((self.ip, self.port)) #绑定要监听的地址（内网ip）和端口, I changed it to blank because I want the server to listen to any ip
        server.listen(5) #开始监听 表示可以使用五个链接排队
        
        print("Started server")
        
        while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
            conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
            print(conn, addr)

            
            try:
                data = str(conn.recv(1024).decode())  #接收数据
                if data:
                    print('Time:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    print('recive:',data)
    
                    if self.esp32Connection(addr):
                        self.readEsp32(addr, data)
                    else:
                        self.checkCommands(data, conn)
            except ConnectionResetError as e:
                print('关闭了正在占线的链接！/ closed busy link?')
                break
            conn.close()
    
    # data should be data.decode()
    def checkCommands(self, data, conn):
        if data == "GET_ALL":
            self.getAll(conn)
        # later if we want to go big
        #elif data == "GET":
        #    get(conn)
        elif bool(re.search("^ADD", data)):
            self.add(data)
    
    def esp32Connection(self, addr):
        if addr[0] in self.esp32Dict:
            return True
        else:
            return False
    
    def getAll(self, conn):
        data_string = json.dumps(self.esp32Dict) #data serialized
        print(self.esp32Dict)
        #data_loaded = json.loads(data) #data loaded
        conn.send(data_string.encode())
    
    def add(self, data):
        print(data)
        newEsp32Addr = re.search("(?<=^ADD)[0-9\.]*", data).group(0)
        self.esp32Dict[newEsp32Addr] = 0
        
    
    # data should be data.decode()
    def readEsp32(self, addr, data):
        self.esp32Dict[addr[0]] = re.search("(?<=Pressure:)[0-9]*", data).group(0)
        print(self.esp32Dict)
        #try:
            #self.esp32Dict[conn[0]] = re.search("(?<=Pressure:)[0-9]*", data)
            #conn.send("Successful".encode())
        #except:
         #   conn.send("Unsuccessful".encode())

