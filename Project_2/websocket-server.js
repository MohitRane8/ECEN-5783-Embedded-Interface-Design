// Node.js WebSocket server script
var mysql = require('mysql');
var mydb = "eid_proj_1";
var mytable = "temp_hum"

var con = mysql.createConnection({
  host: "localhost",
  user: "eiduser",
  password: "beboulder",
  database: mydb
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM " + mytable, function (err, result, fields) {
		if (err) throw err;
    console.log(result);
  });
});


// function dbQuery(cmd) {
// 	// console.log("mysql query: " + cmd);
// 	var res;
//   con.query(cmd, function (err, result, fields) {
//     if (err) throw err;
// 		// console.log(result);
// 		// console.log(result[0]);
// 		res = result[0].temp;
// 		console.log(res);
// 		console.log('typeof' + typeof res);		// typeof is number

// 		res = res.toString();

// 		console.log(res);
// 		console.log('typeof' + typeof res);		// typeof is number

// 		return res;
// 	});
// }

const http = require('http');
const WebSocketServer = require('websocket').server;
const server = http.createServer();
server.listen(9898);

const wsServer = new WebSocketServer({
    httpServer: server
});

wsServer.on('request', function(request) {
    const connection = request.accept(null, request.origin);
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log('Received Message: ' + message.utf8Data);
						
            // get latest temperature and humidity value
            if (message.utf8Data === '1') {
                // connection.sendUTF('test');
                // array to store temperature and humidity values
                var valArray = [];

                // query latest temperature value in database
                con.query("SELECT temperature FROM " + mytable + " ORDER BY ID DESC LIMIT 1", function (err, result, fields) {
                    if (err) throw err;
                    valArray.push(result[0].temperature);
                    console.log('latest temperature: ' + valArray[0]);
                });
                
                // query latest humidity value in database
                con.query("SELECT humidity FROM " + mytable + " ORDER BY ID DESC LIMIT 1", function (err, result, fields) {
                    if (err) throw err;
                    valArray.push(result[0].humidity);
                    console.log('latest humidity: ' + valArray[1]);

                    // send latest temperature and humidity value to client
                    // console.log(valArray);
                    connection.sendUTF(valArray.toString());
                });
            }
                    
            // get last 10 temperature and humidity values
            if (message.utf8Data === '2') {
                // array to store humidity values
                var humArray = [];
                
                // query last 10 humidity values in database
                con.query("SELECT humidity FROM " + mytable + " ORDER BY ID DESC LIMIT 10", function (err, result, fields) {
                    if (err) throw err;

                    // loop to add values obtained from database to humidity array
                    for (i in result) {
                        humArray.push(result[i].humidity);
                    }

                    // send last 10 humidity values to client
                    // console.log(humArray);
                    connection.sendUTF(humArray.toString());
                });
            }

            // connection.sendUTF('Hi this is WebSocket server!');
        }
    });
    connection.on('close', function(reasonCode, description) {
        console.log('Client has disconnected.');
    });
});

wsServer.onmessage = function(e) {
    console.log("Received: '" + e.data + "'");
};
