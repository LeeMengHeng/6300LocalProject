# ESG Project

## Hardware
The hardware part is divided into window detection and human detection inside the classroom. 

* Window Detection:
The application uses pressure sensors to provide real-time monitoring of window pressure data.

* Human Detection:
 This project uses pyroelectric infrared sensors to possibly view the entry and exit of classroom personnel under any lighting conditions.

ESP32 is used as the control center to drive other sensors to work, and at the same time, it uses WiFi to connect to the network and perform socket communication with the back-end server.

## Front End Description

This project is a web application developed using React.js. It includes several key components:

* App.js: The main component that orchestrates the rendering of other components.
* Counter.js: A component that implements a counter functionality.
* Signup.js: A component for user signup functionality.
* SocketCounter.js: A component that demonstrates real-time interaction with a server using WebSockets.

Each of these components is styled with its corresponding CSS file.

## Setup
### Prerequisites

* ESP32 * 2 + Pressure Sensor + Pyroelectric Infrared Sensor * 2
* A USB to TYPE-C data cable used to upload the code
* The computer has Arduino IDE installed and set to ESP32 Dev mode
* A MySQL database that supports public network access
* Node.js installed on your machine.
* A modern web browser.

### Installation
#### Hardware:
Open the `hunandetectionsensor.ino` and `pressureSensor.ino` files, modify the ssid to the WiFi name to be connected, password to the WiFi password, host to `192.168.137.181`, which is the private IP address of the Alibaba Cloud server, and the port to `8000`.

Then upload the `hunandetectionsensor.ino` file to the ESP32 for window detection, and `pressureSensor.ino` file to the ESP32 for human detection.

#### Back End:
- Server: 
The back end entails a single python server, Server_v2.py, that reads in the requests from the esp-32 for both the window pressure sensors and human detection sensor. The server will keep track of the number of people that have entered the room in the people variable. This specified server class has 5 parameters: (notifyTime, windowDict, ip, DoorDict, port) 

    * notifyTime: an int that specifies the number of seconds since the last person has left the room until the specified users are notified in the Twilio datbase. 
    * windowDict: stores the IPs of the window esp-32s and their corresponding window pressure values for each sensor. A value of 0 corresponds to an open window. 
    * ip: this value corresponds to the ip the server is running on.
    * doorDict: stores the IPs of the door esp-32s and their corresponding values for the outside and inside proximity sensor. An off proximity sensor will have a value of 0 while an on value will have a value of 1. Therefore, each door will have 2 values, index 0 being the outside and index 1 being the inside.
    * port: the number represents the server's port.

- API Requests:
    The server allows for 5 main forms of requests: GET_ALL_WINDOWS, GET_ALL_DOORS, GET_PEOPLE, ADD_WINDOW, ADD_DOOR
    * GET_ALL_WINDOWS: if the client sends this message to the server, it will receive the window dictionary values in the form of a string.
    * GET_ALL_DOORS: if the client sends this message to the server, it will receive the door dictionary values in the form of a string.
    * GET_PEOPLE: if the client sends this message to the server, it will receive the number of people in the form of a string
    * ADD_WINDOW: if the client sends this message to the server, it will add a window esp-32 IP 
    * ADD_DOOR: if the client sends this message to the server, it will add a door esp-32 IP

- Database:
To access the MySQL database, access parameters such as public IP and port can be queried in the parameter list of `link`. Add records to the `table_user` table as needed. The data type is int. Among them, the primary key is `gtid`, which cannot be repeated, and `phone_number` represents the user's phone number.

- Notification:
SMS text messages are sent by calling the API of Alibaba Cloud SMS Service. For the interface document, please refer to the following link:
> https://next.api.aliyun.com/document/Dysmsapi/2017-05-25/SendSms?spm=api-workbench.api_explorer.0.0.75cc30c3gFbbx4

#### Front End:
Clone the repository to your local machine.
Navigate to the project directory.
Run npm install to install all the necessary dependencies.

### Running the Application

Start the frontend by running `npm start` in the project directory.
Open your web browser and go to http://localhost:3000 to view the application.

Start the whole client application (React SocketCounter.js and Client.js) by running `npm concurrent start`

**Make sure to adjust the IP address and port number in Client.js to the specified server location.**

## Usage

* Counter Component: Interact with the counter through its UI elements.
* Signup Component: Fill in the required fields to simulate a signup process.
* SocketCounter Component: This component will connect to a WebSocket server and display real-time data. Ensure the server is running and accessible.

## Contributing

* Contributions to this project are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.
