import React, { useState, useEffect} from "react";
import './Counter.css';
import $ from "jquery";


const Counter = () => {
  // useEffect(() => {
  //   // Fetch indicatorCount from your Flask server
  //   fetch('/get-indicator-count')
  //     .then(response => response.json())
  //     .then(data => setIndicatorCount(data.counter1))
  //     .catch(error => console.error('Error fetching indicator count:', error));
  // }, []);
  const [counter1, setCounter1] = useState(0);
  useEffect(() => {
    // Fetch data from the ESP32 server periodically
    const fetchData = async () => {
      try {
        const response = await fetch('172.20.10.2:8000/data'); // Replace with your ESP32 server's URL
        console.log(response.ok)
        if (response.ok) {
          const data = await response.json();
          console.log('fuck you', data);
          // Update the state with the received data
          setCounter1(data.counter1);

        } else {
          // Handle error
        }
      } catch (error) {
        // Handle network or other errors
      }
    };
    console.log(counter1)
    // Fetch data every 5 seconds (adjust the interval as needed)
    const intervalId = setInterval(fetchData, 5000);

    // Clean up the interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  // const utf8EncodeText = new TextEncoder();

  // const str = 'GET_ALL';

  // const byteArray = utf8EncodeText.encode(str);

  // var net = require('net');

  // var client = new net.Socket();
  // client.connect(8000, '172.20.10.2', function() {
  //     console.log('Connected');
  //     client.write(byteArray);
  // });

  // client.on('data', function(data) {
  //     console.log('Received: ' + data);
  //     console.log(data)
  //     client.destroy(); // kill client after server's response
  // });

  $('documnet').ready(function() {
    var counter1 = 0;
    var counter2 = 0;
    var counter3 = 0;
    var light = 1;
    if (counter1 === 0) {
      $('.indicator').css('background-color', 'lightgreen');
    }
    if (counter2 === 0) {
      $('.indicator1').css('background-color', 'lightgreen');
    }
    if (counter3 === 0) {
      $('.indicator2').css('background-color', 'lightgreen');
    }
    if (counter1 > 0) {
      $('.indicator').css('background-color', 'red');
    }
    if (counter2 > 0) {
      $('.indicator1').css('background-color', 'red');
    }
    if (counter3 > 0) {
      $('.indicator2').css('background-color', 'red');
    }
    if (light == 0){
      $('.light').css('background', '#f9f981');
      $('.after').css('border-style', '')
      $('.after').css('border-color', '')
      $('.after').css('background', '#f9f981')
    }
    if (light > 0){
      $('.after').css('border-style', 'solid')
      $('.after').css('border-color', 'black')
      $('.after').css('background', 'white')
      $('.light').css('background', 'black');
    }
});
  return (
<div id="plan">
  
  <div class="room">
    <div class="indicator"></div>
    <div class="indicator1"></div>
    <div class="indicator2"></div>
    <div class="window"></div>
    <div class="window"></div>
    <div class="window"></div>
    <p class="roomName">Classroom</p>
    <div class="simple-bulb">
      <div class="base"></div>
      <div class="light"></div>
      <div class="after"></div>
    </div>
    <div class="door"></div>
  </div>
</div>
  );
};

export default Counter;