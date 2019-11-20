#References: https://www.edureka.co/community/31884/how-to-upload-a-file-in-s3-bucket-using-boto3-in-python
#		   : https://docs.aws.amazon.com/code-samples/latest/catalog/python-rekognition-rekognition-image-python-detect-labels.py.html
#		   : https://docs.aws.amazon.com/lex/latest/dg/API_Operations.html
#		   : https://www.youtube.com/watch?v=KTa1T14nkbw




import boto3
from picamera import PiCamera

aws_access_key_id=ASIATHTWVR4QSES7IZAC
aws_secret_access_key=0plmlj7pgRkJwJBvCgMQsfz0kgUb3rjP5bc7W3mn
aws_session_token=FwoGZXIvYXdzELr//////////wEaDLGFQrL2R/r2oR/MyyLFAWDFKLzzMPl5BtRczBLD6UZ87HjRh/iFgYaoyN4tSsjMYZMlwlwM8gv1EYzT4xKe4f6DKNNL3c3PNLhePzamYzMtj+xLgeGoQhlXFx0osS/NALr+/Wc5liiPiRUxHB0/HvGk+PT7IcKzkyEPEXMhpvHPqqurqcQi9sNZZmMTTQIdTzz98b4e8bjnD54iuLYEKbUq2QqRwBGazcikOzE5uorzoToC1STHDVfUWkxXn3G3hyJ4EzFF0KCLfZOxn3iZ4CWHMyCQKP//0+4FMi3oWudpNqkRntmqL+6EE8ESy54dppywYznbIyzQn2I3g4PI69qFVUd9GJseuP4=

access_key_id     = 'ASIATHTWVR4QSES7IZAC' 
secret_access_key = '0plmlj7pgRkJwJBvCgMQsfz0kgUb3rjP5bc7W3mn'
session_token     = 'FwoGZXIvYXdzELr//////////wEaDLGFQrL2R/r2oR/MyyLFAWDFKLzzMPl5BtRczBLD6UZ87HjRh/iFgYaoyN4tSsjMYZMlwlwM8gv1EYzT4xKe4f6DKNNL3c3PNLhePzamYzMtj+xLgeGoQhlXFx0osS/NALr+/Wc5liiPiRUxHB0/HvGk+PT7IcKzkyEPEXMhpvHPqqurqcQi9sNZZmMTTQIdTzz98b4e8bjnD54iuLYEKbUq2QqRwBGazcikOzE5uorzoToC1STHDVfUWkxXn3G3hyJ4EzFF0KCLfZOxn3iZ4CWHMyCQKP//0+4FMi3oWudpNqkRntmqL+6EE8ESy54dppywYznbIyzQn2I3g4PI69qFVUd9GJseuP4='

camera = PiCamera()
camera.capture('/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/SuperProject/test_image.jpg')

photo = 'test_image.jpg'


s3 = boto3.resource('s3',
					region_name='us-east-1',
					aws_access_key_id=access_key_id,
					aws_secret_access_key=secret_access_key,
					aws_session_token=session_token)

#s3.create_bucket(Bucket = 'omeidsuperproject')

s3.Object('omeidsuperproject','test_image.jpg').upload_file(Filename='/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/SuperProject/test_image.jpg')

client=boto3.client('rekognition',
					region_name='us-east-1',
					aws_access_key_id=access_key_id,
					aws_secret_access_key=secret_access_key,
					aws_session_token=session_token)


response = client.detect_labels(Image={'S3Object':{'Bucket':'omeidsuperproject','Name':photo}},MaxLabels=10)

print('Detected labels for ' + photo) 
print()   
for label in response['Labels']:
	print ("Label: " + label['Name'])
	print ("Confidence: " + str(label['Confidence']))
	print ("Instances:")
	for instance in label['Instances']:
		print ("  Bounding box")
		print ("    Top: " + str(instance['BoundingBox']['Top']))
		print ("    Left: " + str(instance['BoundingBox']['Left']))
		print ("    Width: " +  str(instance['BoundingBox']['Width']))
		print ("    Height: " +  str(instance['BoundingBox']['Height']))
		print ("  Confidence: " + str(instance['Confidence']))
	print()
		
	print ("Parents:")
	for parent in label['Parents']:
		print ("   " + parent['Name'])
	print ("----------")
	print ()

client_polly=boto3.client('polly',
					region_name='us-east-1',
					aws_access_key_id=access_key_id,
					aws_secret_access_key=secret_access_key,
					aws_session_token=session_token)


response = client_polly.synthesize_speech(VoiceId='Joanna',
											OutputFormat='mp3',
											Text = 'The Wand has recognised a abc.')
											
speech_file = open('speech.mp3', 'wb')
speech_file.write(response['AudioStream'].read())
speech_file.close()
