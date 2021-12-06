import ReactDOM from 'react-dom';
import { BrowserRouter, Routes , Route} from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import './css/index.css';
import Home from "./home"
import Restaurants from './restaurants';
import RestaurantPage from './restaurantpage';
import NavBar from "./navbar"
import ClientStatus from './clientstatus';
import 'bootstrap/dist/css/bootstrap.min.css';
// import background from "./img_financedoodle.jpg";


const App = () => {

  const [loggedIn, setLoggedIn] = useState('false');
  const [clientId, setClientId] = useState(null);
  // sessionStorage.setItem("loggedIn", "false");
  // sessionStorage.setItem("clientId", null);
  
  useEffect(() => {
    setLoggedIn(sessionStorage.getItem("loggedIn") === null ? 'false' : sessionStorage.getItem("loggedIn"));
    setClientId(sessionStorage.getItem("clientId"));
    console.log("in effect: " + sessionStorage.getItem("loggedIn") + " " + sessionStorage.getItem("clientId") ) //+ " " +  loggedIn + " " +  clientId
  }, []);

  return (
    <BrowserRouter>
      <div>
        <NavBar loggedIn={loggedIn} setLoggedIn={setLoggedIn}/>
        <Routes>
          <Route exact path="/" element={<Home loggedIn={loggedIn}/>}/>
          {/* <Route exact path="/login" element={<Login loggedIn={loggedIn} setLoggedIn={setLoggedIn} setClientId={setClientId}/>}/> */}
          {/* <Route exact path="/register" element={<Register/>}/> */}
          <Route exact path="/restaurants" element={<Restaurants />}/> 
          <Route path="/restaurants/:index" element={<RestaurantPage />}/>
          <Route exact path="/clientstatus" element={<ClientStatus clientId={clientId}/>}/>       
        </Routes>
      </div>
    </BrowserRouter>
  );

}

// ========================================

ReactDOM.render(
  <App />,
  document.getElementById('root')
);