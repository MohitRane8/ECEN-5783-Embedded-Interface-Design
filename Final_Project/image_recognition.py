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

access_key_id='ASIATHTWVR4Q2RXOSJNV'
secret_access_key='Nl5ugAuRpXcqCweikfy3J32/VkQ7oni9A6TiFnzx'
session_token='FwoGZXIvYXdzEK///////////wEaDAWa+5DE1Hu/YBAlPyLFAV/QgBKm6iQy2pVX1FnjlvS0D5L0nJIu4aubV2NdIBE6bl3q5VMkUjK5ZRzJemJ1jSn2syu3Ojyxnu5JsL9vJgqxeP0swZhsZycbK+7FH+gKONtt3Dq63s44quM9depbG+b/7JC9TVvTdUpI0xmnZavulvxZj6MAM2w1CDhwxPeUdlZ6/d5WRdx/xUj7kAkcmh6FpioaPc2YIl6AUsGbfpvOEyLPyrxijqrmPs7P7eIBGvhM0HNv1WjEYQis2VIh21+GtxgZKLKKwu8FMi19xcgbKzICbC1gEbEhgw2FopNgEYw+necgCIRf0ZcU75+YylsVo3dEVbaMijI='

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
