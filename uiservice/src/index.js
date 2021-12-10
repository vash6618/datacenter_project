import ReactDOM from 'react-dom';
import { BrowserRouter, Routes , Route} from 'react-router-dom';
import React from 'react';
import './css/index.css';
import Home from "./home"
import Restaurants from './restaurants';
import RestaurantPage from './restaurantpage';
import NavBar from "./navbar"
import Analytics from './analytics';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {

  return (
    <BrowserRouter>
      <div>
        <NavBar />
        <Routes>
          <Route exact path="/" element={<Home />}/>
          <Route exact path="/restaurants" element={<Restaurants />}/> 
          <Route path="/restaurants/:index" element={<RestaurantPage />}/>
          <Route exact path="/analytics" element={<Analytics />}/>       
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