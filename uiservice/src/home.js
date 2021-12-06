import React from 'react';
import "./css/home.css"
import { Button, InputGroup, FormControl } from 'react-bootstrap';

const Home = ({loggedIn}) => {

  return (
    <div className="jumbotron vertical-center">
        <div className="container text-center">
            <h1>This is home for FooFi app.</h1>
            <div className="row">
            <InputGroup className="mb-3">
              <FormControl
                placeholder="Search restaurants by name, zip, category"
                aria-label="Restaurant"
                aria-describedby="basic-addon1"
              />
              <Button id="basic-addon1" variant="secondary" size="lg" active>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
              </Button>
            </InputGroup>
            </div>
            <p> Welcome to Manan and Vasu's Online Food Finder Application</p>
            <p> Get access to details and reviews of thousands of restaurant. </p>
            {loggedIn==='false' && 
              <div>
                <p>If you are new here, please register before proceeding with the application form. <br/>If you have been here before, Welcome back!</p>
                <a href="/restaurants">Login now</a>
              </div>
            } <br/>
        </div>
    </div>
  );
}

export default Home;