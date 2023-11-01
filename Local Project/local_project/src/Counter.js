import React, { useState, useEffect} from "react";
import './Counter.css';
import $ from "jquery"
const Counter = () => {
  const [counter1, setIndicatorCount] = useState(0);

  useEffect(() => {
    // Fetch indicatorCount from your Flask server
    fetch('/get-indicator-count')
      .then(response => response.json())
      .then(data => setIndicatorCount(data.counter1))
      .catch(error => console.error('Error fetching indicator count:', error));
  }, []);
  $('documnet').ready(function() {
    var counter1 = 0;
    var counter2 = 0;
    var counter3 = 0;
    if (counter1 == 0) {
      $('.indicator').css('background-color', 'lightgreen');
    }
    if (counter2 == 0) {
      $('.indicator1').css('background-color', 'lightgreen');
    }
    if (counter3 == 0) {
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
    </div>
    <div class="door"></div>
  </div>
</div>
  );
};

export default Counter;