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


access_key_id='ASIATHTWVR4QTCDBMSM5'
secret_access_key='PnlfKlsKEOmIHijx6eqiJ4V8FwaUJXCZMNpf7ZhX'
session_token='FwoGZXIvYXdzEK7//////////wEaDP0M+cyNDlCifpNvpyLFARGl7BALeRyLvaVydzlvm9Toh3DzvYG0e18yuaR87vXOb7C3vzfofqgEG+IiyZ9jGo6+tXOfV3rDxUhF1zBpxBzwnKTUnvYmr5SyFZO3rQwKmyE9Q4milKN902hTgPGEPOJ2IwljI6ES4ADpBJLDGwyrd6cf2yc0V+9ATCzbEn8VoO7JU5ANxXuPZ4P3ueJ2OH+IgYkPtF0Xv8jn5ut35u5zPxdhQvgTGAX6K8MQzkRLIht0EPMGcIGLgazsAJfVmugLsF+tKL7kwe8FMi070r9Oh5x+fJUVeyRaqS/eYheKJvd7edC0EWe0epqQuowRDdU9leGH4rCq3/o='

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
image_capture()
upload_image_to_s3()
obj_detected = extract_labels()
text_to_speech_conversion(obj_detected + 'zzzzzzz')
