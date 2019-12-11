// Author_Name: Mohit Rane
// Date: 11 December 2019
// Project Members: Om Raheja & Mohit Rane
// Embedded Interface Design Final Project
// Magic Wand

// Reference: https://medium.com/@drwtech/a-node-js-introduction-to-amazon-simple-queue-service-sqs-9c0edf866eca

// Load the AWS SDK for Node.js
const AWS = require('aws-sdk');

// AWS configuration of region and credentials
AWS.config.region = 'us-east-1'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-east-1:be5744aa-53a3-47ab-91a6-45a7b1759e8f',
});

// Set the region
AWS.config.update({region: 'us-east-1'});
// SQS Service Object
const sqs = new AWS.SQS({apiVersion: '2012-11-05'});
const accountId = '222513434401';
const queueName = 'my_queue_project_3';
const queueUrl = `https://sqs.us-east-1.amazonaws.com/${accountId}/${queueName}`;
var mysqs = new AWS.SQS();

// mysql setup
var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'eiduser',
  password : 'beboulder',
  database : 'final_proj'
});

// set parameteres for single value receive
var singleRecvParams = {
    QueueUrl: queueUrl,
    AttributeNames: [
        'All'
    ],
    MaxNumberOfMessages: '1',
    VisibilityTimeout: '0',
    WaitTimeSeconds: '1'
};

// set parameters for all values receive
var allRecvParams = {
    QueueUrl: queueUrl,
    AttributeNames: [
        'All'
    ],
    MaxNumberOfMessages: '1',
    VisibilityTimeout: '1',
    WaitTimeSeconds: '1'
};

// set parameters to delete queue
var delQueParams = {
    QueueUrl: queueUrl
};

// set parameters for message count
var attrParams = {
    QueueUrl: queueUrl,
    AttributeNames: [
        'ApproximateNumberOfMessages'
    ]
};

// connect to mysql
connection.connect();

// check for new messages in sqs every 3 seconds
setInterval(function() {
    mysqs.getQueueAttributes(attrParams, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else {
            console.log(data.Attributes.ApproximateNumberOfMessages);

            // receive messages one by one and store it in mysql database
            for (i = 0; i < data.Attributes.ApproximateNumberOfMessages; i++) {						
                // receive message
                mysqs.receiveMessage(allRecvParams, function(err, data) {
                    if (err) console.log(err, err.stack); // an error occurred
                    else {
                        var body = data.Messages[0].Body;
                        console.log(body);

                        // store in database
                        connection.query("INSERT INTO final VALUES ('" + body + "')", function (error, results, fields) {
                            if (error) throw error;
                        });
                                    
                        // delete entry from SQS
                        /*var delParams = {
                            QueueUrl: queueUrl, // required
                            ReceiptHandle: String(data.Messages[0].ReceiptHandle)
                        };
                        mysqs.deleteMessage(delParams, function(err, data) {
                            if (err) console.log(err, err.stack); // an error occurred
                            //else     console.log(data);
                        });*/
                    }
                });
            }
        }
    });
}, 10000);
