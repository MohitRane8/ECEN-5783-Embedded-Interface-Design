#!/usr/bin/env python2.7  
# script by Alex Eames https://raspi.tv/  
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
from speech_to_text import *
from image_recognition import *
import RPi.GPIO as GPIO  



def main():
  GPIO.setmode(GPIO.BCM)  
  
  # GPIO 23 set up as input. It is pulled up to stop false signals  
  GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  print ("Make sure you have a button connected so that when pressed") 
  print ("it will connect GPIO port 23 (pin 16) to GND (pin 6)\n")
  
  #raw_input("Press Enter when ready\n>")
  input("Press Enter when ready\n>")  
  
  print ("Waiting for falling edge on port 23")  
  # now the program will do nothing until the signal on port 23   
  # starts to fall towards zero. This is why we used the pullup  
  # to keep the signal high and prevent a false interrupt  
  
  print ("During this waiting time, your computer is not")
  print ("wasting resources by polling for a button press.\n")
  print ("Press your button when ready to initiate a falling edge interrupt.")  
  try:  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    print ("\nFalling edge detected. Now your program can continue with")  
    print ("whatever was waiting for a button press.")
    record()
    save_audio()
    text = speech_to_text_conversion()
    print("Interrupt = " + text )
    if text == "Okay, Capturing Image":
      image_capture()
      upload_image_to_s3()
      obj_detected = extract_labels()
      text_to_speech_conversion(obj_detected + 'zzzzzzz')
      print(obj_detected)

  except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit 




#record()
#save_audio()
#speech_to_text_conversion()



if __name__ == "__main__":
  main()
