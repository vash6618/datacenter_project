import React from 'react';
import { Badge, Card } from 'react-bootstrap';

const RestaurantCard = ({restaurant, index}) =>  {

    return (
        <div>
            <Card style={{ width: '20rem' }} key={index}>
            <Card.Img variant="top" src={restaurant["image_url"]} style={{height: '16rem'}}/>
            <Card.Body>
                <Card.Title>{restaurant["name"]}</Card.Title>
                <Card.Text>
                    Address: {restaurant["address"]} <br/>
                    Phone: {restaurant["phone"]} <br/>
                    Rating: {restaurant["rating"]} <br/>
                    {restaurant["categories"].map((cat, index) => <Badge bg="warning" text="dark" key={index} style={{marginRight:"5px"}}>{cat}</Badge> )}
                    <br/>
                    <a href={"/restaurants/"+(restaurant["id"]-1)}> Local Page </a>
                </Card.Text>
            </Card.Body>
            </Card>
            <br/>
        </div>
    );

}

export default RestaurantCard;


