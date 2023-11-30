import './Counter.css';
import $ from "jquery";


var counter1 = 0;
var counter2 = 0;
var counter3 = 0;
var light = 1;
  
const SocketCounter = () => {

    $('documnet').ready(function() {
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

        if (light > 0){
          $('.light').css('background', '#f9f981');
          $('.after').css('border-style', '')
          $('.after').css('border-color', '')
          $('.after').css('background', '#f9f981')
        }
        if (light === 0){
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
    
    export default SocketCounter;
