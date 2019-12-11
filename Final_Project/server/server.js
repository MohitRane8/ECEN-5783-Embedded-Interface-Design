// Reference: https://medium.com/@drwtech/a-node-js-introduction-to-amazon-simple-queue-service-sqs-9c0edf866eca

// Load the AWS SDK for Node.js
const AWS = require('aws-sdk');

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

var i;
for(i=0; i<7; i++)
{
    mysqs.receiveMessage(singleRecvParams, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else {				
            console.log(data.Messages[0].Body);
        }
    });
}

// // get single value from SQS on button click and delete that entry from SQS		
// // receive message
// mysqs.receiveMessage(singleRecvParams, function(err, data) {
//     if (err) console.log(err, err.stack); // an error occurred
//     else {				
//         // log full data
//         // console.log(data);
//         // log body
//         console.log(data.Messages[0].Body);

//         // delete entry from SQS
//         var delParams = {
//             QueueUrl: queueUrl, // required
//             ReceiptHandle: String(data.Messages[0].ReceiptHandle)
//         };
//         mysqs.deleteMessage(delParams, function(err, data) {
//             if (err) console.log(err, err.stack); // an error occurred
//             else     console.log(data);
//         });
//     }
// });

// // // get number of messages in SQS
// // mysqs.getQueueAttributes(attrParams, function(err, data) {
// //     if (err) console.log(err, err.stack); // an error occurred
// //     else {
// //         console.log(data.Attributes.ApproximateNumberOfMessages);
        
// //         var timeArray = [];
// //         var tempArray = [];
// //         var humArray = [];
// //         //var array = [20][3];
// //         for (i = 0; i < data.Attributes.ApproximateNumberOfMessages; i++) {						
// //             // receive message
// //             mysqs.receiveMessage(allRecvParams, function(err, data) {
// //                 if (err) console.log(err, err.stack); // an error occurred
// //                 else {
// //                     if ( typeof mysqs.receiveMessage.counter == 'undefined' ) {
// //                         mysqs.receiveMessage.counter = 0;
// //                     }
                    
// //                     ++mysqs.receiveMessage.counter;
// //                     console.log("counter = %d", mysqs.receiveMessage.counter);

// //                     // log full data
// //                     //console.log(data);
// //                     // log JSON body having timestamp, temperature and humidity values
// //                     //console.log(data.Messages[0].Body);
// //                     // parse JSON object
// //                     var reqParams = JSON.parse(data.Messages[0].Body);
                    
// //                     // store parameters in array								
// //                     timeArray[mysqs.receiveMessage.counter%20] = reqParams.timestamp;
// //                     tempArray[mysqs.receiveMessage.counter%20] = reqParams.temperature;
// //                     humArray[mysqs.receiveMessage.counter%20] = reqParams.humidity;
                    
// //                     // set temperature values according to required units
// //                     if(tempUnitFlag == 1) {
// //                         tempArray[mysqs.receiveMessage.counter%20] = tempArray[mysqs.receiveMessage.counter%20]*1.8+32;
// //                     }
                    
// //                     console.log("timestamp [%d] = %s", i, timeArray[mysqs.receiveMessage.counter%20]);
// //                     console.log("temperature [%d] = %f", i, tempArray[mysqs.receiveMessage.counter%20]);
// //                     console.log("humidity [%d] = %f", i, humArray[mysqs.receiveMessage.counter%20]);
                                   
// //                     // delete entry from SQS
// //                     var delParams = {
// //                         QueueUrl: queueUrl, // required
// //                         ReceiptHandle: String(data.Messages[0].ReceiptHandle)
// //                     };
// //                     mysqs.deleteMessage(delParams, function(err, data) {
// //                         if (err) console.log(err, err.stack); // an error occurred
// //                         else     console.log(data);
// //                     });
                    
// //                 }
// //             });
// //         }
        
// //     }
// // });
    
// // get number of messages in SQS
// mysqs.getQueueAttributes(attrParams, function(err, data) {
//     if (err) console.log(err, err.stack); // an error occurred
//     else {
//         //console.log(data);
//         console.log(data.Attributes.ApproximateNumberOfMessages);
//     }
// });