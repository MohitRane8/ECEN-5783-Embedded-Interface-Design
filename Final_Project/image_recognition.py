'''
@ Author(s)_Name: Om Raheja & Mohit Rane
@ Date: 11 December 2019
@ Embedded Interface Design Super Project
@ The magic Wand
@ References: Text-to-Speech (https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html)

'''

# Imports
import boto3
import os
import sys
from picamera import PiCamera
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import subprocess
from tempfile import gettempdir


# Credentials required to create clients for services
access_key_id='ASIATHTWVR4QYPCGCGBQ'
secret_access_key='fcjBYIA0iKGnz65gW+tdFTFanDpQ7hpX0yZ6ILBR'
session_token='FwoGZXIvYXdzEL3//////////wEaDFEo24+7pqrl2Q/U3CLFAXVS4m8FOj8tFn9KfDlYJUgIHv8u+fnUdjESo1raJirWU4n3AtWhjuF1YGUuwSkB9gHWash0Vn62yaU2VmTUIIzl0AOBx5gjBElgL0ua7dTEQcwYS2sTO7BjujXYT9JehKqh3WhKlAaoED410cCHcIow6HnMnf9XItQrvJ+NAvDw2N3vt2A1nPKN8TYN27VNkRmv226C0rr+NiqqzNuVYt8zgUKcxsKybNFL699c2KA3LuvRqI+fyY3AHkYhgDih9eUkGPgNKJWHxe8FMi17wG7nvHcMg4epsKIQi2Mm3x2zLX7nYoxUYndNmzOj5JxShxQhFdcXlfa2/Bg='


# Create Client for Polly
session = boto3.Session(region_name='us-east-1',
						aws_access_key_id=access_key_id,
						aws_secret_access_key=secret_access_key,
						aws_session_token=session_token)
polly = session.client("polly",region_name='us-east-1')


'''
@ Function Name : image_capture()
@ Brief         : Captures images
@ Param in      : void
@ Return        : None 

'''
def image_capture():
	camera.capture('image.jpg')


'''
@ Function Name : upload_image_to_s3()
@ Brief         : Upload image captured to s3
@ Param in      : void
@ Return        : None 

'''
def upload_image_to_s3():
	#Create bucket only once
	#s3.create_bucket(Bucket = 'omeidsuperproject')
	
	s3 = boto3.resource('s3',
					region_name='us-east-1',
					aws_access_key_id=access_key_id,
					aws_secret_access_key=secret_access_key,
					aws_session_token=session_token)
	s3.Object('omeidsuperproject','image.jpg').upload_file(Filename='/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/Final_Project/image.jpg')


'''
@ Function Name : extract_labels()
@ Brief         : Extract labels generated by Image rekognition service for an image
@ Param in      : void
@ Return        : None 

'''
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
	
	
'''
@ Function Name : text_to_speech_conversion()
@ Brief         : Convert text to speech
@ Param in      : text to be converted to speech
@ Return        : None 

'''				
def text_to_speech_conversion(text):
	# Request speech synthesis
	response = polly.synthesize_speech(Text=text, OutputFormat="mp3",VoiceId="Joanna")
	speech_file = open('speech.mp3', 'wb')
	speech_file.write(response['AudioStream'].read())
	speech_file.close()
	subprocess.call(['xdg-open', 'speech.mp3'])


				

camera = PiCamera()
