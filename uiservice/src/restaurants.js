import React, { useState, useEffect } from 'react';
import RestaurantCard from './restaurantcard';
import './css/restaurants.css'
import InfiniteScroll from "react-infinite-scroll-component";


const Restaurants = () =>  {

    const [items, setItems] = useState(null)
    const [offset, setOffset] = useState(0)
    const my_pod_ip = process.env["REACT_APP_POD_IP"];

    useEffect(() => {
        if(items === null && offset === 0) {
          fetch('http://'+my_pod_ip+':5005/restaurants?limit=6&offset='+offset, {
          }
          ).then(res => res.json()).then(data => {
            console.log("Data: ", data)
            setItems(data.restaurants)
            setOffset(offset+6)
          }).catch(err => {
            throw new Error(err)
          });
        }
      }, [items, offset, my_pod_ip]);
    
    const fetchMoreData = () => {
        console.log("calling fetch more data")
        fetch('http://'+my_pod_ip+':5005/restaurants?limit=6&offset='+offset
        ).then(res => res.json()).then(data => {
            console.log("Data: ", data)
            setItems(items.concat(data.restaurants))
            setOffset(offset+6)
        }).catch(err => {
            throw new Error(err)
        });
    };
    
    const list_restaurants = (restaurant, index) => {
        return (<RestaurantCard restaurant={restaurant} index={index} className="mr-3"/>);
    }
    
    return (
        <div className="pad">
            <h1>Browse Restaurants</h1>
            <br/>
            <div> 
                <InfiniteScroll
                    dataLength={items === null ? 0 : items.length}
                    next={fetchMoreData}
                    hasMore={true}
                    loader={<h4>Loading...</h4>}
                    >
                    {items === null ? null : items.map(list_restaurants)}
                </InfiniteScroll>
            </div>
        </div>
    );

}

export default Restaurants;