
class Client {
 
  constructor(host, port, message) {
    const net = require('node:net');

    this.client = new net.Socket();
    this.client.connect({ port: port, host: host ?? "localhost" })

    this.client.on('connect', () => {
      console.log('Connected to the server!');
      this.client.write(message);
    });

    this.client.on('data', (data) => {
      console.log('Received data:', data.toString());
      const fs = require('fs');
      fs.writeFile(message + '.txt', data, (err) => {
          if (err) {
              console.error('Error writing data to file:', err);
          } else {
              console.log('Data saved to file.');
          }
      });
    });
    
    
    this.client.on('error', (error) => {
      console.error('Error occurred:', error);
    });
    
   this.client.on('close', () => {
    console.log('Connection closed.');
    this.client.destroy();
    });

    
  }

  
}


host = "10.12.2.58"
var i = 0;
function go () {
    var check = new Client(host, 8000, "GET_ALL_WINDOWS");
    var check = new Client(host, 8000, "GET_ALL_DOORS");
    var check = new Client(host, 8000, "GET_PEOPLE");
    setTimeout(go, 2000); // callback
}
go();





// const client3 = new Client("192.168.1.101", 8000, "GET_PEOPLE");