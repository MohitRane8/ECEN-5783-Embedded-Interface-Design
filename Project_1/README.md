# EMBEDDED INTERFACE DESIGN - PROJECT 1
## PROJECT MEMBERS
    Om Raheja
    Mohit Rane
## BRIEF OVERVIEW OF THE PROJECT
    Temperature and Humidity monitoring system using DHT22 sensor
    The project aims at demonstrating a rapid prototype development of a temperature and humidity monitoring system. The project makes use     of various tools listed below:
    1) Pyqt5 for GUI development
    2) MySQL for database management
    
    Features of the project include:
    1) Acquire Temperature and Humidity from DHT22 sensor periodically every 15 seconds.
    2) Current Temperature and Humidity values can be obtained using a Push Button embedded in the GUI.
    3) The Temperature and Humidity values are stored in a database that is created using MySQL.
    4) The GUI includes a status line indicating messages based on the comparison of current values of
       Temperature and Humidity with their respective thresholds.
    5) The GUI also includes a graphic window showing plots of Temperature and Humidity by retrieving 
       the last ten entries in the database on a button push.
    6) After 30 iterations, the application gracefully exits.

## INSTALLATION INSTRUCTIONS
    1) Before downloading the Project-1 folder on your system, make sure to have the
       following installed:
       a) Python3
       b) pip
       c) pyqt5
       d) MySQL
       This link [https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/] will help you setup 
       python3 and pip. It also includes a python code to interface the DHT22 sensor with the raspberry pi.
  
    2) Once you have the above installed, clone the Project-1 folder from the repository.
    3) From the downloaded folder, find the 'src' folder.
    4) Run prototype_1.py with the help of the following command:
       "$python3 prototype_1.py"
    5) After running the above command, a Graphical User Interface (GUI) will show up.
    6) The GUI consists of all the functionality mentioned in the initial part of the documentation.
    
## PROJECT CONTRIBUTIONS
    Om Raheja: Responsible for developing the Graphical User Interface and binding it with functionality needed.
    Mohit Rane: Created the database needed to store the data using MySQL. 
    Integration of the GUI functionality with the Database was performed by both the project members.
    
## PROJECT ADDITIONS
    A push button was added to change the units of Temperature from Celsisu to Fahrenheit and vice-versa. 
    On pressing that button on the GUI, all the temperature values changed from Celsius to Fahrenheit. 
    If the button was pressed multiple times, the unit of Temperature shifts from one to the other.
