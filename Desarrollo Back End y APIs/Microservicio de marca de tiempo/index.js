// index.js
// where your node app starts

// init project
var express = require('express');
var app = express();

// enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// so that your API is remotely testable by FCC 
var cors = require('cors');
app.use(cors({optionsSuccessStatus: 200}));  // some legacy browsers choke on 204

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (req, res) {
  res.sendFile(__dirname + '/views/index.html');
});

// date... 
app.get("/api/:date?", function (req, res) {
  let param1 = req.params.date;    
  let date = new Date(param1);
  console.log(param1);
  console.log(date);
  
  if (param1 == undefined) {
    let now = new Date();
    res.json({unix: now.getTime(), utc: now.toUTCString()});
  } else if (date != "Invalid Date") {
    res.json({unix: date.getTime(), utc: date.toUTCString()});
  } else if (new Date(Number(param1)).toUTCString() != "Invalid Date") {
    res.json({unix: Number(param1), utc: new Date(Number(param1)).toUTCString()});
  } else {
    res.json({ error : "Invalid Date" });
  }
});

// listen for requests :)
var listener = app.listen(process.env.PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
