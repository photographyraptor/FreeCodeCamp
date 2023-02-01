const express = require('express')
const app = express()
const cors = require('cors')
const bodyParser = require("body-parser");
require('dotenv').config()

app.use(cors())
app.use(express.static('public'))
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html')
});
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

//----------------------DATA--------------------------
const usersData = [];
const logsData = [];

//--------------------ENDPOINTS------------------------

app.get('/api/users/:_id/:logs?', (req, res) => {
  if (req.method === 'GET') {
    console.log("getLogs");
    let data = GetUserLogs(req);
    res.json(data);
  }
});

app.post('/api/users/:_id/:exercices?', (req, res) => {
  if (req.method === 'POST') {
    console.log("postLog");
    let data = PostLog(req);
    res.json(data);
  }
});

app.get('/api/users', (req, res) => {
  if (req.method === 'GET') {
    if (req.params._id) {
      next();
    } else {
      console.log("getApiUser");
      res.json(usersData);
    }    
  } else {
    next();
  }
});

app.post('/api/users', (req, res) => {
  if (req.method === 'POST') {
    if (req.params._id) {
      next();
    } else {
      console.log("postApiUser");
      let newUser = PostUser(req);
      res.json(newUser);
    }
  } else {
    next();
  }
});

//----------------------FUNCTIONS-----------------------

function PostUser(req) {
  let nUser = {
    username: req.body.username,
    _id: (usersData.length).toString()
  };
  usersData.push(nUser);
  return nUser;
}

function GetUserLogs(req) {
  const userId = req.params._id;
  let fetchUser = FetchUser(userId);
  let fetchLogs = FetchLogs(userId, req);
  fetchUser.log = fetchLogs;
  fetchUser.count = fetchUser.log.length;
  return fetchUser;
}

function PostLog(req) {
  let formattedDate = (new Date(req.body.date)).toDateString();
  let nLog = {
    username: FetchUser(req.params._id).username,
    description: req.body.description,
    duration: Number(req.body.duration),
    date:
      formattedDate != "Invalid Date"
      ? formattedDate
      : (new Date()).toDateString(),
    _id: (req.params._id).toString()
  };
  logsData.push(nLog);
  return nLog;
}

//---------------INTERNAL-----------------------

function FetchUser(userId) {
  for(let i=0; i<usersData.length; i++) {
    if (usersData[i]._id == userId) {
      return {
        username: usersData[i].username,
        _id: usersData[i]._id.toString(),
        log: []
      };
    }
  }
}

function FetchLogs(userId, req) {
  const from = req.query.from;
  const to = req.query.to;
  const limit = req.query.limit;
  let fetchLogs = [];
  
  for(let i=0; i<logsData.length; i++) {
    if (logsData[i]._id == userId) {
      let fetchLog = {
        description: logsData[i].description,
        duration: logsData[i].duration,
        date: logsData[i].date
      };
      fetchLogs.push(fetchLog);
    }
  }

  if (from && to) {
    fetchLogs = fetchLogs
      .filter(l =>
        new Date(l.date) >= new Date(from) &&
        new Date(l.date) <= new Date(to));
  }
  if (limit) {
    fetchLogs = fetchLogs.slice(0, limit);
  }
  
  return fetchLogs;
}

//-----------------------------------------------------

const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})
