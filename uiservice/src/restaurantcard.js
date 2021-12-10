import React from 'react';
import { Button, Badge, Card } from 'react-bootstrap';

const RestaurantCard = ({restaurant, index}) =>  {

    return (
        <div>
            <Card style={{ width: '60rem', display: 'flex', flexDirection: 'row' }} key={index}>
            <Card.Img variant="horizontal" src={restaurant["image_url"]} style={{width: '20rem', height: '16rem'}}/>
            <Card.Body>
                <Card.Title>{restaurant["name"]}</Card.Title>
                <Card.Text>
                    Address: {restaurant["address"] + " " + restaurant["city"] + " " + restaurant["state"] + " " + restaurant["zip_code"]} <br/>
                    Phone: {restaurant["phone"]} <br/>
                    Rating: {restaurant["rating"]} <br/>
                    {restaurant["categories"].map((cat, index) => <Badge bg="warning" text="dark" key={index} style={{marginRight:"5px"}}>{cat}</Badge> )}
                    <br/>
                    <Button href={"/restaurants/"+(restaurant["id"]-1)} className="mt-3" size="sm"> More Information </Button>
                </Card.Text>
            </Card.Body>
            </Card>
            <br/>
        </div>
    );

}

export default RestaurantCard;


