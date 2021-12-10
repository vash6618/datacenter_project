import React, { useState } from 'react';
import "./css/home.css"
import { Badge, Button, InputGroup, FormControl } from 'react-bootstrap';

const Home = () => {
  const [searchtext, setSearchText] = useState("")
  const [searchresults, setSearchResults] = useState([])
  const my_pod_ip = process.env["REACT_APP_POD_IP"];

  const onChangeHandler = (e) => {
    setSearchText(e.target.value)
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ "search_term": e.target.value })
    };
    fetch('http://'+my_pod_ip+':5005/search_restaurants', requestOptions
    ).then(res => res.json()).then(data => {
        console.log("Data: ", data)
        setSearchResults(data.restaurants)
    }).catch(err => {
        throw new Error(err)
    });
  }

  const show_restaurants = (restaurant, index) => {
    return (<ul key={index}>
              <a href={"/restaurants/"+(restaurant["id"]-1)}>
                <Badge bg="primary" style={{width:'30em'}}> {restaurant["name"]} </Badge>
              </a>
            </ul>);
  }

  return (
    <div className="jumbotron vertical-center">
        <div className="container text-center">
            <h1>Welcome to FooFi app!</h1>
            <p> Manan and Vasu's Online Food Finder Application</p>
            <p> Get access to details and reviews of thousands of restaurant. </p>
            
            <div>
              <p>Head over to discover new <a href="/restaurants">restaurants</a>!</p>
              <p>Find local <a href="/analytics">analytics</a>!</p>
            </div>
            <br/>

            <div className="row">
            <InputGroup className="mb-3">
              <FormControl
                placeholder="Search restaurants by name, zip, category"
                aria-label="Restaurant"
                aria-describedby="basic-addon1"
                value={searchtext}
                onChange={onChangeHandler.bind(this)}
              />
              <Button id="basic-addon1" variant="secondary" size="lg" active>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
              </Button>
            </InputGroup>
            </div>
            {
              searchresults.length === 0 ?
              <div></div>
              :
              <div>{searchresults.map(show_restaurants)}</div>
            }
        </div>
    </div>
  );
}

export default Home;