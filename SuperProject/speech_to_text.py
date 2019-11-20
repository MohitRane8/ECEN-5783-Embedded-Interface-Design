import boto3
import wave


access_key_id     = 'ASIATHTWVR4QSES7IZAC' 
secret_access_key = '0plmlj7pgRkJwJBvCgMQsfz0kgUb3rjP5bc7W3mn'
session_token     = 'FwoGZXIvYXdzELr//////////wEaDLGFQrL2R/r2oR/MyyLFAWDFKLzzMPl5BtRczBLD6UZ87HjRh/iFgYaoyN4tSsjMYZMlwlwM8gv1EYzT4xKe4f6DKNNL3c3PNLhePzamYzMtj+xLgeGoQhlXFx0osS/NALr+/Wc5liiPiRUxHB0/HvGk+PT7IcKzkyEPEXMhpvHPqqurqcQi9sNZZmMTTQIdTzz98b4e8bjnD54iuLYEKbUq2QqRwBGazcikOzE5uorzoToC1STHDVfUWkxXn3G3hyJ4EzFF0KCLfZOxn3iZ4CWHMyCQKP//0+4FMi3oWudpNqkRntmqL+6EE8ESy54dppywYznbIyzQn2I3g4PI69qFVUd9GJseuP4='



client_lex = boto3.client('lex-runtime',
							region_name='us-east-1',
							aws_access_key_id= access_key_id,
							aws_secret_access_key=secret_access_key,
							aws_session_token=session_token)
							
audio_file = wave.open('/home/pi/Documents/ECEN-5783-Embedded-Interface-Design/SuperProject/test1.wav','rb')

response_from_lex = client_lex.post_content(botName = 'eid_test',
											botAlias = 'stt',
											userId = 'omraheja',
											contentType = 'audio/l16;rate=16000;channels=1',
											accept = 'text/plain;charset=utf-8',
											inputStream = audio_file.readframes(96044)
											)
											
											
print(response_from_lex['message']);
