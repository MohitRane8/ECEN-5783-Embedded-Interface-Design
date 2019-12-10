import boto3
import os
import sys
from picamera import PiCamera
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import subprocess
from tempfile import gettempdir


access_key_id     = 'ASIATHTWVR4Q3MPK6YGU'
secret_access_key = '9+Ot1LToufjHaMl3XCSlimLUqJcob3/ZZQCzXcvl'
session_token     = 'FwoGZXIvYXdzEJ7//////////wEaDOpdDUGYqOEdWqH7cyLFAaiR5Q77H5C/qRAmKZjgSivaP/cMxKIjItCfNxnyn/4CJFa+cQB3UbUYeCFJ9+xPC/Ak+/hgOm1bqUtvnwtOwamct3xtHeHIfRXXlFNRb4v8fxCDFyvj5IKbBmtlvfFHy4kuThf/G28RVHmHjcj5bC72yzE9uxYBplLIaA+3gzkC7zU3aI3IHwwHRifzU/enH/8U8TqMvcVAbH+7ydIMpYaFTsLT986Y7N3sNj1m03oqlL5NZFMCbP8xdjjNI0mYW84UnDAqKJuUvu8FMi0VxTHKNDB4CEeFXL09sdEZW5UrMrHqhehGu1M9mDFkiZsEz/pFNaDWtD11sXI='

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
