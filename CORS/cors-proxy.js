const express = require('express');
const request = require('request');

const app = express();

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
    res.header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
    // res.header("Access-Control-Allow-Headers: Content-Type, Authorization");
    next();
});

app.get('/', (req, res) => {
    return "CORS index";
});

app.get('/restaurants', (req, res) => {
  console.log(`request for on restaurants`)
  request(
    { url: 'http://34.66.95.129:5001/restaurants?limit='+req.query.limit+'&offset='+req.query.offset },
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: error });
      }
      res.json(JSON.parse(body));
    }
  )
});

app.post('/search_restaurants', (req, res) => {
  console.log(`request for on search_restaurants`)
  request(
    { 
      url: 'http://34.66.95.129:5001/search_restaurants',
      body: req,
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      } 
    },
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: error });
      }
      res.json(JSON.parse(body));
    }
  )
});

const PORT = 5005;
app.listen(PORT, () => console.log(`listening on ${PORT}`));