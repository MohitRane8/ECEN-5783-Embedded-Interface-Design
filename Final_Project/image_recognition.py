import boto3
from picamera import PiCamera


access_key_id     = 'ASIATHTWVR4Q5L3PUREU'
secret_access_key = '76lHzTwE9/1pk9d/fKkIt6ZSE5BOEaHhWYitwWCa'
session_token     = 'FwoGZXIvYXdzEJ3//////////wEaDGiU8TFdxneDyXGTuyLFAa35awzcVHy1YT/9bm9w6Vq4WkBCDu/rakUQZFtCRHqzJO3goErVMosHbgfRurXclP8+VH/wd28Iuwbylg+TzoK20JId4HE/mWRd2ofxd5iOJiq8jfg2spXn0t2j22dXYs9ZxjNJvYHqz7IxX7RZJTNe3iDtGY9Kw8S8SOL5XPJ+LHMWSV7ASHTBSFI/vzehkNkic50/pm7jovn2rCr0ZjgONc9P8OJCVpbtVar8fGmo/4nulmWzJl94TMjXGka3XIunM+JpKLn5ve8FMi3Jpm2DB21wN1Ej8BKbefmeosyNDSS5o4UFfzgscTEdjSwu6jkh0qQZSjqwbZY='


def image_capture():
	camera.capture('image.jpg')


#def create_s3_bucket():
	#Create bucket only once
	#s3.create_bucket(Bucket = 'omeidsuperproject')
	
	#s3 = boto3.resource('s3',
	#				region_name='us-east-1',
	#				aws_access_key_id=access_key_id,
	#				aws_secret_access_key=secret_access_key,
	#				aws_session_token=session_token)


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
					
					
					
					

camera = PiCamera()
image_capture()
#create_s3_bucket()
upload_image_to_s3()
extract_labels()
