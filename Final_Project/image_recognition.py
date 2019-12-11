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

access_key_id='ASIATHTWVR4QUUQ5T3ZX'
secret_access_key='kb/dMBxXuv6xghwr82LZng3liAVAzy1Y1kR+gnUp'
session_token='FwoGZXIvYXdzELr//////////wEaDJH7yKl1e4tEetY4byLFAWkFxnGxrsgwbgW71PtXAgKvVVBPSDJPf9DBnpy/saWlKP4pqn+X8irrafdRTgpCFEzm5AF/P1Xo8Ys8Gis8iBx9hXA+YB2zpUVlTgLRpjJ8khhpmAezM7e6auyWkzjNdxROE/Z6Lk2BC/hRvShYk/QPo6YGyBAJm0L3BYraRYYH2QIh3rHB3KMa2oOZznTeS+67vzOn+BRd2PCbYfjhRgDDa9Lz92x8QdAOWmtGfDmxhDb4OT7lTgOjKtwlWG9wbZnYx8LkKPWxxO8FMi1DSPJwLCuetzGjUpCSUaBz3mmAn/FxXF4O/xi2i5IHVXQyNlkOUgff85q3LRo='

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
