import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
	temperature,humidity = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
	
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(humidity, temperature))
	else:
		print("Failed to retrieve data from humidity sensor")
