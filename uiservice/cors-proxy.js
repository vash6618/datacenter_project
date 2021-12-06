const express = require('./node_modules/express');
const request = require('./node_modules/request');

const app = express();

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
    res.header("Access-Control-Allow-Headers: Content-Type, Authorization");
    next();
});

app.get('/', (req, res) => {
    return "CORS index";
});

app.get('/restaurants', (req, res) => {
  request(
    { url: 'http://34.133.182.120:5001/restaurants?limit='+req.query.limit+'&offset='+req.query.offset},
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: err.message });
      }
      res.json(JSON.parse(body));
    }
  )
});

const PORT = 5005;
app.listen(PORT, () => console.log(`listening on ${PORT}`));