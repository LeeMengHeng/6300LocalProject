import socket
import datetime
import json
import re
import time

import pymysql
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

# Steps:
# To use command prompts, start the MacOS Terminal app and enter one of the following commands: 
# 1. “ipconfig getifaddr en1” - The system will return the IP address for a wired Ethernet connection. 
# 2. “ipconfig getifaddr en0” - This will return the IP address of your wireless connection.



class Server_v2:
    # address = '192.168.137.39'
    # the ip is your device's ip 
    # notifyTime is in seconds
    def __init__(self, notifyTime = 1, windowDict = {"192.168.137.25": ['0', '0']}, ip='192.168.137.181', doorDict={'192.168.137.35': ['0', '0']}, port = 8000):
        #self.password = password
        #self.address = address
        self.ip = ip
        self.port = port
        self.windowDict = windowDict
        self.doorDict = doorDict
        self.people = 1
        self.tempTime = -1
        self.timeOnDoor2 = -1
        self.timeOnDoor1 = -1



        # Check if a notification message was sent
        self.messageSent = False

        # How long until staff is notified of no one in the room
        self.notifyTime = notifyTime
        # Time of when last person left the room
        self.timeLastLeft = 0; 
        
        self.num_list = []

        self.sig_door = 'SMS_464116180'
        self.sig_window = 'SMS_464096123'

        access_key_id = "LTAI5tK9NnCjUCgDuDrbsFYo"
        access_key_secret = "yK9iLuOYSuTzyo28XwPcPJCQ8fIrpa"


        self.client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')

        link=pymysql.connect(
            host = 'gz-cynosdbmysql-grp-6ml1wj8z.sql.tencentcdb.com'
            ,user = 'root'
            ,passwd='652398Aq'
            ,port= 27898
            ,db='project'
            ,charset='utf8'
        )

        cur = link.cursor()
        sql="SELECT phone_number FROM table_user WHERE phone_number is not null"
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            self.num_list.append(i[0])
        cur.close()
        link.close()
    
    def start(self):
        
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server.bind((self.ip, self.port))
        server.listen(5) 
        
        print("Started server")
        


        while True:# conn
            conn,addr = server.accept() 
        #print(conn)
            
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
                
                if self.messageSent == False:
                    self.checkMessage()
                else:
                    if self.people > 0:
                        self.messageSent = False
                
            except ConnectionResetError as e:
                print('closed busy link?')
                break
            conn.close()
    
    def checkMessage(self):
        if self.people == 0 and self.convertDatetime(datetime.datetime.now()) - self.timeLastLeft > self.notifyTime:
            self.messageSent = True
            for num in self.num_list:
                self.send_message(num, self.sig_door)

            for key in self.windowDict.keys():
                for elem in self.windowDict[key]:
                    if elem == "0":
                        for num in self.num_list:
                            self.send_message(num, self.sig_window)
                        break

    # data should be data.decode()
    def checkCommands(self, data, conn):
        if str(self.ip) + ":" + str(self.port) in data:
            #self.encode(conn)
            conn.send("Server says hello!".encode())
        elif data == "GET_ALL_WINDOWS":
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
        data_string = json.dumps(int(self.people)) #data serialized
        #print(self.doorDict)
        #data_loaded = json.loads(data) #data loaded
        conn.send(data_string.encode())
    
    def getAllWindows(self, conn):
        data_string = json.dumps(self.windowDict[list(self.windowDict.keys())[0]]) #data serialized
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
                if self.people == 0:
                    self.timeLastLeft = self.convertDatetime(datetime.datetime.now())
        else:
            if re.search("(?<=Door_1:)[0-9]*", data) != None:
                self.doorDict[addr[0]][0] = re.search("(?<=Door_1:)[0-9]*", data).group(0)
                self.timeOnDoor1 = self.convertDatetime(datetime.datetime.now())
                
            if re.search("(?<=Door_2:)[0-9]*", data) != None:
                self.doorDict[addr[0]][1] = re.search("(?<=Door_2:)[0-9]*", data).group(0)
                self.timeOnDoor2 = self.convertDatetime(datetime.datetime.now())
        if self.people < 0:
            self.people = 0
        
        
    # data should be data.decode()
    def readWindow(self, addr, data):
        if re.search("(?<=Pressure_1:)[0-9]*", data) != None:
            self.windowDict[addr[0]][0] = re.search("(?<=Pressure_1:)[0-9]*", data).group(0)
        if re.search("(?<=Pressure_2:)[0-9]*", data) != None:
            self.windowDict[addr[0]][1] = re.search("(?<=Pressure_2:)[0-9]*", data).group(0)
            
    def convertDatetime(self, dt):
        return time.mktime((dt).timetuple()) + (dt).microsecond/1e6 

    def send_message(self, phone_num, sig):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', phone_num)
        request.add_query_param('SignName', "room")
        request.add_query_param('TemplateCode', sig)
        request.add_query_param('TemplateParam', "{\"code\":\"12345\"}")

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))


test = Server_v2()
test.start()