
import React, {useState, useEffect} from "react";
import './Counter.css';
import $ from "jquery";
import people from './GET_PEOPLE.txt';
import windows from './GET_ALL_WINDOWS.txt';


// windows is a list and people is one int for there are people inside or there aren't
const SocketCounter = () => {
  const [fetchedPeopleText, setFetchedPeopleText] = useState('');
  const [fetchedWindowText, setFetchedWindowText] = useState('');

  useEffect(() => {
    const readFile = () => {

        fetch(people)
        .then(r => r.text())
        .then(text => {
          console.log('text decoded:', text);
          setFetchedPeopleText(text);
        });
        fetch(windows)
        .then(r => r.text())
        .then(text => {
          console.log('text decoded:', text);
          setFetchedWindowText(text);
        });
    
      };
  
    const interval = setInterval(readFile, 100); // Call readFile every 5 seconds (5000 milliseconds)
  
    // Clean up the interval when the component unmounts
    return () => clearInterval(interval);
  }, []); // Empty dependency array ensures this effect runs only once when the component mounts
  var stopBlinking = false;


  function blink(selector) {
      $(selector).fadeOut('slow', function() {
          $(this).fadeIn('slow', function() {
              if (!stopBlinking)
              {
                  blink(this);
              }
              else
              {
                  $(this).hide();
              }
          });
      });
  }
blink(".exc");

$('documnet').ready(function() {
  var counter1 = parseInt(JSON.parse(fetchedWindowText)[0]);
  var counter2 = parseInt(JSON.parse(fetchedWindowText)[1]);
  var counter3 = 100;
  var light = parseInt(fetchedPeopleText);
  if (counter1 !== 0) {
    $('.indicator').css('background-color', 'lightgreen');
  }
  if (counter2 !== 0) {
    $('.indicator1').css('background-color', 'lightgreen');
  }
  if (counter3 !== 0) {
    $('.indicator2').css('background-color', 'lightgreen');
  }
  if (counter1 === 0) {
    $('.indicator').css('background-color', 'red');
  }
  if (counter2 === 0) {
    $('.indicator1').css('background-color', 'red');
  }
  if (counter3 === 0) {
    $('.indicator2').css('background-color', 'red');
  }
  if (light === 0){
    $('.exc').css('color', 'white');
  }
  if (light >= 1){
    $('.exc').css('color', 'red');
  }
  // if (light == 0){
  //   $('.light').css('background', '#f9f981');
  //   $('.after').css('border-style', '')
  //   $('.after').css('border-color', '')
  //   $('.after').css('background', '#f9f981')
  // }
  // if (light > 0){
  //   $('.after').css('border-style', 'solid')
  //   $('.after').css('border-color', 'black')
  //   $('.after').css('background', 'white')
  //   $('.light').css('background', 'black');
  // }
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
      <div class="exc">!</div>
    </div>
    <div class="door"></div>
  </div>
</div>
  );
};

export default SocketCounter;

