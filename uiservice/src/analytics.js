import React, { useState } from 'react';
import { Card, Form } from 'react-bootstrap';

const Analytics = () => {
    const [img_url1, setImgURL1] = useState('https://storage.googleapis.com/datacenter-analysis//srv/price_vs_restaurants_1.png');
    const [img_url2, setImgURL2] = useState('https://storage.googleapis.com/datacenter-analysis//srv/restaurants_vs_price_1.png');
    
    const [radio1, setRadio1] = useState(1);
    const [radio2, setRadio2] = useState(1);
    
    const price = ['$', '$$', '$$$', '$$$$']
    const rating = ['1-2', '2-3', '3-4', '4-5']
    
    const onChangeRadio1 = (e) => {
        var new_val = parseInt(e.target.value)
        setRadio1(new_val)
        setImgURL1('https://storage.googleapis.com/datacenter-analysis//srv/price_vs_restaurants_'+e.target.value+'.png')
    }
    const onChangeRadio2 = (e) => {
        var new_val = parseInt(e.target.value)
        setRadio2(new_val)
        setImgURL2('https://storage.googleapis.com/datacenter-analysis//srv/restaurants_vs_price_'+e.target.value+'.png')
    }

    return (
        <div className="pad">
            <h1>Restaurant Insights</h1>
            <div style={{display: 'flex'}}>
            <Card style={{ width: '30rem', justifyContent: "center", alignItems: "center", marginRight: "3em"}}>
                <Card.Body>
                    <Form>
                        <div key={`inline-radio`} className="mb-3">
                        Price:&nbsp;
                        <Form.Check inline label="$" value="1"
                            checked={radio1 === 1}
                            onChange={onChangeRadio1}
                            name="group1" type='radio' id={`inline-radio-1`}/>
                        <Form.Check inline label="$$" value="2"
                            checked={radio1 === 2}
                            onChange={onChangeRadio1}
                            name="group1" type='radio' id={`inline-radio-2`} />
                        <Form.Check inline label="$$$" value="3"
                            checked={radio1 === 3}
                            onChange={onChangeRadio1}
                            name="group1" type='radio' id={`inline-radio-3`} />
                        <Form.Check inline label="$$$$" value="4"
                            checked={radio1 === 4}
                            onChange={onChangeRadio1}
                            name="group1" type='radio' id={`inline-radio-4`} />
                        </div>
                    </Form>
                </Card.Body>
                <Card.Img variant="top" src={img_url1} />
                <Card.Body>
                    <Card.Text>
                    Rating distribution for price ({price[radio1-1]})
                    </Card.Text>
                </Card.Body>
            </Card>
            <Card style={{ width: '30rem', justifyContent: "center", alignItems: "center"}}>
                <Card.Body>
                    <Form>
                        <div key={`inline-radio2`} className="mb-3">
                        Rating:&nbsp;
                        <Form.Check inline label="1-2" value="1"
                            checked={radio2 === 1}
                            onChange={onChangeRadio2}
                            name="group2" type='radio' id={`inline-radio2-1`}/>
                        <Form.Check inline label="2-3" value="2"
                            checked={radio2 === 2}
                            onChange={onChangeRadio2}
                            name="group2" type='radio' id={`inline-radio2-2`} />
                        <Form.Check inline label="3-4" value="3"
                            checked={radio2 === 3}
                            onChange={onChangeRadio2}
                            name="group2" type='radio' id={`inline-radio2-3`} />
                        <Form.Check inline label="4-5" value="4"
                            checked={radio2 === 4}
                            onChange={onChangeRadio2}
                            name="group2" type='radio' id={`inline-radio2-4`} />
                        </div>
                    </Form>
                </Card.Body>
                <Card.Img variant="top" src={img_url2} />
                <Card.Body>
                    <Card.Text>
                    Price distribution for rating ({rating[radio2-1]})
                    </Card.Text>
                </Card.Body>
            </Card> 
            </div>
        </div>
    );
}

export default Analytics;