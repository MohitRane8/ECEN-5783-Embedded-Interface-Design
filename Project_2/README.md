# EMBEDDED INTERFACE DESIGN - PROJECT 2
## PROJECT MEMBERS
    Om Raheja
    Mohit Rane
## BRIEF OVERVIEW OF THE PROJECT
    Temperature and Humidity monitoring system using DHT22 sensor(PyQt5,NodeJS,Tornado,MySQL,MatPlotlib,CSS,HTML)
    The project aims at demonstrating a rapid prototype development of a temperature and humidity monitoring
    system. The project makes use of various tools listed below:
    1) PyQt5 for GUI development (Adapted from Project 1)
    2) MySQL for database management (Adapted from Project 1)
    3) HTML for developing client side of the system
    4) Tornado Server for interacting with Python application (GUI)
    5) NodeJS Server for interacting with MySQL databse
    
    Additional Features of the project include:
    1) The application developed in Project 1 functions entirely the same way as it did earlier.
    2) HTML webpage interacting with two server, tornado and nodeJS.
    3) Webpage includes the following features:
       a) Push Button to acquire latest temperature and humidity values from python application through tornado server.
       b) Push Button to acquire latest temperature and humidity values from MySQL database through NodeJS server.
       c) Push Button to acquire performance analysis of both servers (tornado and NodeJS).
       d) Pair of buttons to acquire graphs (temperature and humidity) from the python application and display them
          on the html webpage.
    4) On disconnecting the sensor, the html page indicates "Sensor Disconnected".

## INSTALLATION INSTRUCTIONS
    1) Before downloading the Project-2 folder on your system, make sure to have the
       following installed:
       a) Python3
       b) pip
       c) PyQt5
       d) MySQL
       e) tornado
       This link [https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/] will help you setup 
       python3 and pip. It also includes a python code to interface the DHT22 sensor with the raspberry pi.
  
    2) Once you have the above installed, clone the Project-2 folder from the repository.
    3) Run the 'starter.sh' script with the help of the following command:
       "$sh starter.sh" or "$./starter.sh"
       This will ensure that all the servers get started and establish connection.
    5) After running the above command, a Graphical User Interface (GUI) will show up along with terminals running tornado
       and NodeJS servers.
    6) Click on the project2.html to open the web page.
    7) On opening the html page, the NodeJS server gets connected with the html client. For establishing connection with the 
       tornado server, press the "open" button on the webpage.
    8) After all the above steps, the user can interact with the application.
    
## PROJECT CONTRIBUTIONS
    Om Raheja: Responsible for setting up the html webpage along with its interaction with the tornado server.
    Mohit Rane: Developed the NodeJS server and its interaction with the html client.
    Code Integration, Error Checking, Scripting to run all files at once and Project Documentation was done by both
    the team members.
    
## PROJECT ADDITIONS
    A push button was added to change the units of Temperature from Celsius to Fahrenheit and vice-versa. 
    On pressing that button on the HTML webpage, all the temperature values changed from Celsius to Fahrenheit. 
    If the button was pressed multiple times, the unit of Temperature shifts from one to the other.
