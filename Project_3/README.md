# EMBEDDED INTERFACE DESIGN - PROJECT 3
## PROJECT MEMBERS
    Om Raheja
    Mohit Rane
## BRIEF OVERVIEW OF THE PROJECT
    Temperature and Humidity monitoring system using DHT22 sensor(PyQt5,NodeJS,MySQL,MatPlotlib,CSS,HTML,Amazon Web Services)
    The project aims at demonstrating a rapid prototype development of a temperature and humidity monitoring
    system. The project makes use of various tools listed below:
    1) PyQt5 for GUI development (Adapted from Project 1)
    2) MySQL for database management (Adapted from Project 1)
    3) HTML for developing client side of the system
    4) Amazon Web Services (SQS,SNS,Lambda Function, AWS IoT Core)
    
    Additional Features of the project include:
    1) The application developed in Project 1 and Project 2 functions entirely the same way as it did earlier.
    2) HTML webpage interacts with SQS queues which transfers data messages.
    3) Webpage includes the following features:
       a) Push Button to acquire a single SQS record.
       b) Push Button to acquire all SQS record.
       c) A table to display messages pulled out from the SQS queue.
       d) Displays the number of records currently in the SQS queue.

## INSTALLATION INSTRUCTIONS
    1) Before downloading the Project-3 folder on your system, make sure to have the
       following installed:
       a) Python3
       b) pip
       c) PyQt5
       d) MySQL
       e) tornado
       This link [https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/] will help you setup 
       python3 and pip. It also includes a python code to interface the DHT22 sensor with the raspberry pi.
  
    2) Once you have the above installed, clone the Project-3 folder from the repository.
    3) To open the GUI, run the command "python3 prototype.py"
    4) After running the above command, a Graphical User Interface (GUI) will open up showing the temperature and humidity readings.
    6) The latest values and periodic values are displayed on the GUI. These values are also sent to the SQS and SNS based on the message type (data or alert). The data message is passed to the AWS SQS queue which is then displayed on the HTML webpage. The alert message will be sent to the AWS SNS which then sends a e-mail notification.  
       
## PROJECT CONTRIBUTIONS
    Om Raheja: Responsible for parsing data and alert messages to the AWS IoT via MQTT. Configured AWS Lambda to pass the messages to AWS SQS queue and AWS SNS depending upon the type of message.
    Mohit Rane: Developed HTML page to account for the data messaged being received from the SQS Queue. Integrated the code along with error checking.
    Project documentation was done by both the team members.
    
## PROJECT ADDITIONS
    A push button was added to change the units of Temperature from Celsius to Fahrenheit and vice-versa. 
    On pressing that button on the HTML webpage, all the temperature values changed from Celsius to Fahrenheit. 
    If the button was pressed multiple times, the unit of Temperature shifts from one to the other.
    HTML page displays the number of records currently in the SQS queue. This request displays the count in a text field.
    
## REFERENCES
    Pi to AWS IoT:
    • https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html
    • https://techblog.calvinboey.com/raspberrypi-aws-iot-python/
    SQS with HTTP GET and POST requests: 
    • https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html
    Using Lambda with SNS:
    • https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html
    Using Lambda with SQS:
    • https://startupnextdoor.com/adding-to-sqs-queue-using-aws-lambda-and-a-serverless-api-endpoint/
    HTML syntax and example: https://www.w3schools.com/
    Populating data in table (HTML): https://www.youtube.com/watch?v=40qreu8Al7o

## PROJECT ISSUES
    A lot of time was spent to figure out how to use the AWS services.
    A lot of online material had to be referred beyond the documentation that was provided.
    The HTML-SQS interface via HTTP took more time than expected.
    While populating the table on the HTML page, use of global variable in a function was giving unexpected results. After referring to several websites, that issue was fixed. By that, we understood the scoping of variables in javascript.
    
    
