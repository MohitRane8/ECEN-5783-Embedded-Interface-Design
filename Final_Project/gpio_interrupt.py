#!/usr/bin/env python2.7  
# script by Alex Eames https://raspi.tv/  
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
from speech_to_text import *
from image_recognition import *
import RPi.GPIO as GPIO  

queue_url = 'https://sqs.us-east-1.amazonaws.com/222513434401/my_queue_project_3'



sqs = boto3.client('sqs',\
					region_name='us-east-1',\
					aws_access_key_id=access_key_id,\
					aws_secret_access_key=secret_access_key,\
					aws_session_token=session_token)



def record_again():
  try:  
    GPIO.wait_for_edge(24, GPIO.FALLING)  
    print ("\nFalling edge detected. Now your program can continue with")  
    print ("whatever was waiting for a button press.")
    record('response.wav')
    #save_audio('response.wav')
    text_1 = speech_to_text_conversion('response.wav')
    print("Interrupt = " + text_1 )
    global string
    if text_1 == "Correct":
      string = string + 'correct'
      print(string)
    elif text_1 == "wrong":
      #global string
      string = string + 'wrong'
      print(string)
    else:
      string = string + 'invalid_input'
      print(string)
      
    response = sqs.send_message(QueueUrl=queue_url,DelaySeconds=10,MessageBody=string)
    string = ''
  except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  







def main():
  GPIO.setmode(GPIO.BCM)  
  
  # GPIO 23 set up as input. It is pulled up to stop false signals  
  GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  
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
    record('command.wav')
  
    #save_audio('command.wav')
  
    text = speech_to_text_conversion('command.wav')
    
    print("Interrupt = " + text )
    
    if text == "Identifio":
      global string
      string = string + "Identifio" + ','
      print("string1 = " + string)
      image_capture()
      upload_image_to_s3()
      obj_detected = extract_labels()
      string = string + obj_detected + ','
      print(string)               # identifio , face/human...
      text_to_speech_conversion(obj_detected + 'zzzzzzz')
      print(obj_detected)
  except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

  record_again()

#GPIO.cleanup()           # clean up GPIO on normal exit 




#record()
#save_audio()
#speech_to_text_conversion()



if __name__ == "__main__":
  while True:
    main()
