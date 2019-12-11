# References: Text-to-Speech (https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html)
import boto3
import os
import sys
from picamera import PiCamera
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import subprocess
from tempfile import gettempdir


access_key_id='ASIATHTWVR4QZ7QCNLNO'
secret_access_key='2bbg11e9u0X+uBzDpQpizU/GWMHv8Vz4GeOgVuP4'
session_token='FwoGZXIvYXdzELT//////////wEaDPZOa/Ct5aR9vjvo+yLFAS20RdhkPTeyc1DIUUSbmHdDrZEkwDgZow297/0AzXBEJSma/HA6iwy6otJCOEM2XPvJ/5H3ItHrwEy8NfSWERez6wGMq+3Q9Yo5sJ5DFMb1SWTBMgz1WgoeM/GrKBx5bOdnsZt9u1Lulj69W9c1eInAM2tTJHaxDVXxpGKaADH+Uif0aZUioViNP6ZRLyg57x5Iaxv6fhwCIOs1dWbo+i241UFhfZ8MG8Z3qtz4onDymWFFVvlKdROFkrvZjzH1qx9Brn0yKNyMw+8FMi2jAq20Yj5iduKlEI+PmkEr6nHeFfwiZHS212HWf9jbfzeXQI3FPXa5NNy8doA='

session = boto3.Session(region_name='us-east-1',
						aws_access_key_id=access_key_id,
						aws_secret_access_key=secret_access_key,
						aws_session_token=session_token)
polly = session.client("polly",region_name='us-east-1')


def image_capture():
	camera.capture('image.jpg')


def upload_image_to_s3():
	#Create bucket only once
	#s3.create_bucket(Bucket = 'omeidsuperproject')
	
	s3 = boto3.resource('s3',
					region_name='us-east-1',
					aws_access_key_id=access_key_id,
					aws_secret_access_key=secret_access_key,
					aws_session_token=session_token)
	s3.Object('omeidsuperproject','image.jpg').upload_file(Filename='/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Final_Project/image.jpg')


def extract_labels():
	client=boto3.client('rekognition',
						region_name='us-east-1',
						aws_access_key_id=access_key_id,
						aws_secret_access_key=secret_access_key,
						aws_session_token=session_token)
						
						
	response = client.detect_labels(Image={'S3Object':{'Bucket':'omeidsuperproject','Name':"image.jpg"}},MaxLabels=10)
	
	for label in response['Labels']:
		print("Labels = " + label['Name'])
		print("Confidence = " + str(label['Confidence']))
		
		if int(label['Confidence']) > 90:
			return label['Name']
					
def text_to_speech_conversion(text):
	# Request speech synthesis
	response = polly.synthesize_speech(Text=text, OutputFormat="mp3",VoiceId="Joanna")
	speech_file = open('speech.mp3', 'wb')
	speech_file.write(response['AudioStream'].read())
	speech_file.close()
	subprocess.call(['xdg-open', 'speech.mp3'])


				

camera = PiCamera()
#image_capture()
#upload_image_to_s3()
#obj_detected = extract_labels()
#text_to_speech_conversion(obj_detected + 'zzzzzzz')
