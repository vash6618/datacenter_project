import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './css/restaurants.css'
import { Badge } from 'react-bootstrap';


const RestaurantPage = () =>  {
    var {index} = useParams();
    console.log("Params: ", index);
    const [restaurant, setRestaurant] = useState(null);
    const my_pod_ip = process.env["REACT_APP_POD_IP"];
    useEffect(() => {
        console.log("Using effect1...", my_pod_ip)
        if(restaurant === null) {
          fetch('http://'+my_pod_ip+':5005/restaurants?limit=1&offset='+index, {
          }
          ).then(res => res.json()).then(data => {
            console.log("Data: ", data)
            setRestaurant(data.restaurants[0])
          }).catch(err => {
            throw new Error(err)
          });
        }
      }, [restaurant, index, my_pod_ip]);
    
    if (restaurant === null) {
        return (
            <div className="pad">
                <h4>Loading...</h4>
            </div>
        );
    }
    return (
        <div className="pad">
            <h1>{restaurant["name"]}</h1>
            <div className="row mb-3">
                <div className="col-sm-2">Rating: {restaurant["rating"]} <br/></div>
                <div className="col-sm-2">Review Count: {restaurant["review_count"]} <br/></div>
                <div className="col-sm-1">Price: {restaurant["price"]} <br/></div>
            </div>
            <img className="mb-3" src={restaurant["image_url"]} style={{ width: '28rem', height: '22rem' }} alt=""/>
            <div>
                {restaurant["categories"].map((cat, index) => <Badge bg="warning" text="dark" key={index} style={{marginRight:"5px"}}>{cat}</Badge> )} <br/>
                Address: {restaurant["address"]} <br/>
                Phone: {restaurant["phone"]} <br/>
            </div>
        </div>
    );
}

export default RestaurantPage;


