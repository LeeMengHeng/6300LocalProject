import socket
import datetime
import json
import re
import time

# Steps:
# To use command prompts, start the MacOS Terminal app and enter one of the following commands: 
# 1. “ipconfig getifaddr en1” - The system will return the IP address for a wired Ethernet connection. 
# 2. “ipconfig getifaddr en0” - This will return the IP address of your wireless connection.



class Server:
    # address = '192.168.137.39'
    # the ip is your device's ip 
    def __init__(self, windowDict = {"192.168.137.30": ['0', '0']}, ip='192.168.137.71', doorDict={'192.168.137.219': [0, 0]}, port = 8000):
        #self.password = password
        #self.address = address
        self.ip = ip
        self.port = port
        self.windowDict = windowDict
        self.doorDict = doorDict
        self.people = 0
        self.tempTime = -1
        self.timeOnDoor2 = -1
        self.timeOnDoor1 = -1
        
        
    
    def start(self):
        
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server.bind((self.ip, self.port))
        server.listen(5) 
        
        print("Started server")
        
        while True:# conn
            conn,addr = server.accept() 
            
            try:
                data = str(conn.recv(1024).decode())  
                if data:
                    print('Time:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    print('receive:',data)
                    print()
    
                    if self.windowConnection(addr):
                        self.readWindow(addr, data)
                    elif self.doorConnection(addr):
                        self.readDoor(addr, data)
                    else:
                        self.checkCommands(data, conn)
            except ConnectionResetError as e:
                print('closed busy link?')
                break
            conn.close()
    
    # data should be data.decode()
    def checkCommands(self, data, conn):
        if data == "GET_ALL_WINDOWS":
            self.getAllWindows(conn)
        elif data == "GET_ALL_DOORS":
            self.getAllDoors(conn)
        elif data == "GET_PEOPLE":
            self.getPeopleCount(conn)
        elif bool(re.search("^ADD_WINDOW", data)):
            self.addWindow(data)
        elif bool(re.search("^ADD_DOOR", data)):
            self.addWindow(data)
            
    
    def windowConnection(self, addr):
        if addr[0] in self.windowDict:
            return True
        else:
            return False
        
    def doorConnection(self, addr):
        if addr[0] in self.doorDict:
            return True
        else:
            return False
    
    def getPeopleCount(self, conn):
        data_string = json.dumps(self.people) #data serialized
        #print(self.doorDict)
        #data_loaded = json.loads(data) #data loaded
        conn.send(data_string.encode())
    
    def getAllWindows(self, conn):
        data_string = json.dumps(self.windowDict) #data serialized
        #print(self.doorDict)
        #data_loaded = json.loads(data) #data loaded
        conn.send(data_string.encode())
        
    def getAllDoors(self, conn):
        data_string = json.dumps(self.doorDict) 
        #print(self.doorDict)
        conn.send(data_string.encode())
        
    
    def addWindow(self, data):
        #print(data)
        newWindowAddr = re.search("(?<=^ADD_WINDOW)[0-9\.]*", data).group(0)
        self.windowDict[newWindowAddr] = 0
        
    def addDoor(self, data):
        newWindowAddr = re.search("(?<=^ADD_DOOR)[0-9\.]*", data).group(0)
        self.doorDict[newWindowAddr] = 0
        
    # data should be data.decode()
    def readDoor(self, addr, data):
        if self.doorDict[addr[0]][1] == "1" and self.doorDict[addr[0]][0] == "1":
            if re.search("(?<=Door_1:)[0-9]*", data) != None:
                self.doorDict[addr[0]][0] = re.search("(?<=Door_1:)[0-9]*", data).group(0)
            else:
                self.doorDict[addr[0]][1] = re.search("(?<=Door_2:)[0-9]*", data).group(0)
            
            if self.doorDict[addr[0]][0] == "0":
                self.people += self.convertDatetime(datetime.datetime.now()) - self.timeOnDoor1;
            else:
                self.people -= self.convertDatetime(datetime.datetime.now()) - self.timeOnDoor2;
        else:
            if re.search("(?<=Door_1:)[0-9]*", data) != None:
                self.doorDict[addr[0]][0] = re.search("(?<=Door_1:)[0-9]*", data).group(0)
                self.timeOnDoor1 = self.convertDatetime(datetime.datetime.now())
                
            if re.search("(?<=Door_2:)[0-9]*", data) != None:
                self.doorDict[addr[0]][1] = re.search("(?<=Door_2:)[0-9]*", data).group(0)
                self.timeOnDoor2 = self.convertDatetime(datetime.datetime.now())
        
    # data should be data.decode()
    def readWindow(self, addr, data):
        if re.search("(?<=Pressure_1:)[0-9]*", data) != None:
            self.windowDict[addr[0]][0] = re.search("(?<=Pressure_1:)[0-9]*", data).group(0)
        if re.search("(?<=Pressure_2:)[0-9]*", data) != None:
            self.windowDict[addr[0]][1] = re.search("(?<=Pressure_2:)[0-9]*", data).group(0)
            
    def convertDatetime(self, dt):
        return time.mktime((dt).timetuple()) + (dt).microsecond/1e6 

    
test = Server()
test.start()
