# EMBEDDED INTERFACE DESIGN - SUPER PROJECT (MAGIC WAND)
## PROJECT MEMBERS
    Om Raheja
    Mohit Rane
## BRIEF OVERVIEW OF THE PROJECT
    The magic wand consists of 3 major components:
    Client Raspberry Pi, AWS services and Server Raspberry Pi
    
    Client Raspberry Pi: The microphone records input from the user. This audo is sent to the AWS Lex service to 
    convert audio file to text file. This text is sent as a command to the Camera to perform the appropriate task.
    Image captured by the camera is sent to AWS image rekognition service for identification. On identification
    of image, a label is returned to the Rpi. This label is then sent to AWS Polly service to convert the text to
    speech which is then output by a speaker.
    
    AWS Services: The services used were Speech-to-Text, Text-to-Speech and Image Rekognition
    
    Server Raspberry Pi: This runs a PyQt GUI to interact with the system and get the statistics of the data acquired.
    The data is retreived from the SQL databse.
   
    1) PyQt5 for GUI development (Adapted from Project 1)
    2) MySQL for database management (Adapted from Project 1)
    3) NodeJS Server for querying data from SQS queue to SQL database.
    
    Additional Features of the project include:
    A GPIO trigger to initiate recording of either command or response.

## COMPILATION INSTRUCTIONS
    1) Before downloading the Final_Project folder on your system, make sure to have the
       following installed:
       a) Python3
       b) pip
       c) PyQt5
       d) MySQL  
    2) Once you have the above installed, clone the Final_Project folder from the repository.
    3) Open 3 terminals. Run GUI on the first by running the following command ($python3 new_gui.py).
    4) On the second terminal run the Node.js server using the following command ($node server.js)
    5) On the last terminal, run the application using ($python3 gpio_interrupt.py)
    6) After all the above steps, the user can interact with the application.
    7) To give command, Connect GPIO 23 of Rpi to GND.
    7) To give response to Rpi, connect GPIO 24 of Rpi to GND. 
    
## INSTALLATION INSTRUCTIONS
    1) Update packages on Raspberry Pi:
    sudo apt-get update
    sudo-apt-get-upgrade
    2) MySQL:
    sudo apt install mariadb-server
    3) Pyqt5:
    sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
    4) AWS SDK:
    pip3 install AWSIoTPythonSDK
    
## PROJECT CONTRIBUTIONS
    Om Raheja: 
    Integrated AWS services, Image rekognition, Polly, Lex with application.
    Implemented Voice to text and Text to Voice application
    Sent data to SQS so that Server can fetch it to run its internal application.
    
    Mohit Rane:
    Developed the NodeJS server and its interaction with the SQL database
    Developed Pyqt GUI and its functionality

    Code Integration, Error Checking, Scripting to run all files at once and Project Documentation was done by both
    the team members.
   
## REFERENCES
    Interaction between NodeJS and MySQL: https://www.w3schools.com/nodejs/nodejs_mysql.asp
    NodeJS Webserver Example: https://www.pubnub.com/blog/nodejs-websocket-programmingexamples/
    Python-Tornado-HTML example: https://os.mbed.com/cookbook/Websockets-Server
    HTML syntax and example: https://www.w3schools.com/
    Populating data in table (HTML): https://www.youtube.com/watch?v=40qreu8Al7o
    TimeStamp example (HTML): https://www.w3schools.com/jsref/jsref_gettime.asp
    Draw IO: https://www.draw.io/
    Balsamiq: https://balsamiq.com/
    UML: https://www.geeksforgeeks.org/unified-modeling-language-uml-sequence-diagrams/
    Boto3: https://www.edureka.co/community/31884/how-to-upload-a-file-in-s3-bucket-using-boto3-in-python
    Image Recognition: https://docs.aws.amazon.com/code-samples/latest/catalog/python-rekognition-rekognition-image-python-detect-labels.py.html
    Amazon Lex: https://docs.aws.amazon.com/lex/latest/dg/API_Operations.html , https://www.youtube.com/watch?v=KTa1T14nkbw
    Reference for GPIO Interrupt: https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio 
    Reference for TTS converesion: https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html
    MySQL + QT + Python: https://www.youtube.com/watch?v=2TibG64zLeA 
    AWS NodeJS: https://docs.aws.amazon.com/sdk-for-javascript/index.html
