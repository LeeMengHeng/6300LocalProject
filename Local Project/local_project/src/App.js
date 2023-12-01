// import logo from './logo.svg';
// import './App.css';
// import Signup from './Signup';
// import SocketCounter from "./SocketCounter";
// import {BrowserRouter, Routes, Route} from 'react-router-dom';

// function App() {

//   return (
//     <div>
//       <div className="App">
//         <Signup/>
//       </div>
//     </div>
//   );
  
// }

// export default App;

import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Signup from './Signup';
import Counter from './SocketCounter';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path="/socket-counter" element={<Counter />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
