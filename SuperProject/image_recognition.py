#References: https://www.edureka.co/community/31884/how-to-upload-a-file-in-s3-bucket-using-boto3-in-python
#		   : https://docs.aws.amazon.com/code-samples/latest/catalog/python-rekognition-rekognition-image-python-detect-labels.py.html
#		   : https://docs.aws.amazon.com/lex/latest/dg/API_Operations.html
#		   : https://www.youtube.com/watch?v=KTa1T14nkbw




import boto3
from picamera import PiCamera


#[default]
#aws_access_key_id=ASIATHTWVR4QQSJ5XZ4A
#aws_secret_access_key=+DOANvLXcjDiR05Vby1XhkMtsyybcNUi1UM684bF
#aws_session_token=FwoGZXIvYXdzEMn//////////wEaDP0QO350NAYd9xITcSLFAeQj/sSAHjtuN6LzAu3kWQZykBMotNtM1wAVFBUe98Bd0mvXo4AV+6dDwxeOFYQe/wu3+TWv+6h48HuA9PShwg7WbQGJMQhJGV2Ib5zxoBHaFLbVsYHVDIoCokgxY4+8Reoie5issUD5ESMJ6BB5afI8eGkLgmwSWpQ1fbrZXUjmFjmErJ985/NgAbo2XY2rgcYEq3hcHbKFFUCS4YyKd0z/Oe3Bp3ThayfSDbCvLwX6/lFko8stDvy0spQTUj0FUGmyQnvMKISh1+4FMi3mEngVFPKPtitqbPwK51ON6PTCPaFAFtnvo4tl5gDHvhRrjwnlvkaoW4Y0qy0=


access_key_id     = 'ASIATHTWVR4QQSJ5XZ4A' 
secret_access_key = '+DOANvLXcjDiR05Vby1XhkMtsyybcNUi1UM684bF'
session_token     = 'FwoGZXIvYXdzEMn//////////wEaDP0QO350NAYd9xITcSLFAeQj/sSAHjtuN6LzAu3kWQZykBMotNtM1wAVFBUe98Bd0mvXo4AV+6dDwxeOFYQe/wu3+TWv+6h48HuA9PShwg7WbQGJMQhJGV2Ib5zxoBHaFLbVsYHVDIoCokgxY4+8Reoie5issUD5ESMJ6BB5afI8eGkLgmwSWpQ1fbrZXUjmFjmErJ985/NgAbo2XY2rgcYEq3hcHbKFFUCS4YyKd0z/Oe3Bp3ThayfSDbCvLwX6/lFko8stDvy0spQTUj0FUGmyQnvMKISh1+4FMi3mEngVFPKPtitqbPwK51ON6PTCPaFAFtnvo4tl5gDHvhRrjwnlvkaoW4Y0qy0='

camera = PiCamera()
camera.capture('/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/SuperProject/test_image.jpg')

image = 'test_image.jpg'


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


response = client.detect_labels(Image={'S3Object':{'Bucket':'omeidsuperproject','Name':image}},MaxLabels=10)

print('Detected labels for ' + image) 
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
