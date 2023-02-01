require('dotenv').config();
const express = require('express');
const bodyParser = require("body-parser");
const cors = require('cors');
const app = express();

// Basic Configuration
const port = process.env.PORT || 3000;

// Urls
let urls = {
};

// parse
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use(cors());

app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

app.get('/api/shorturl/:short', function(req, res) {
  for(let url in urls) {
    if (urls[url] == req.params.short) {
      res.redirect(url);
    }
  }
});

app.post('/api/shorturl', (req, res) => {
  let reg = /^(ftp|http|https):\/\/[^ "]+$/;
  if (req.body.url == "" || !reg.test(req.body.url)) {
    res.json({ error : 'invalid url'});
  }
  for(let url in urls) {
    if (url == req.body.url) {
      res.json({ original_url : url, short_url : urls[url]});
    }
  }
  console.log(Object.keys(urls));
  urls[req.body.url] = Object.keys(urls).length > 0
    ? urls[Object.keys(urls)[Object.keys(urls).length - 1]] + 1
    : 0;
  res.json({ original_url : req.body.url, short_url : urls[req.body.url]});
});

app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
