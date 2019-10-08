/*@Author_Name: Mohit Rane
 *@Date: 22 September 2019
 *@Project Members: Om Raheja & Mohit Rane
 *@Embedded Interface Design Project 1
 *@Temperature and Humidity monitoring system (Tornado server, NodeJS server and HTML client) *
 * */

/* Node.js WebSocket server script */
var mysql = require('mysql');
var mydb = "eid_proj_1";
var mytable = "prototype_table"

var con = mysql.createConnection({
  host: "localhost",
  user: "eiduser",
  password: "beboulder",
  database: mydb
});

con.connect(function(err) {
  if (err) throw err;
});


const http = require('http');
const WebSocketServer = require('websocket').server;
const server = http.createServer();
server.listen(9898, '128.138.189.73');

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
                        humArray.push(result[9-i].humidity);
                    }
                    
                    connection.sendUTF(humArray.toString());
                });
            }
        }
    });
    connection.on('close', function(reasonCode, description) {
        console.log('Client has disconnected.');
    });
});

wsServer.onmessage = function(e) {
    console.log("Received: '" + e.data + "'");
};
