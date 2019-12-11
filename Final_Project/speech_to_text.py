'''
@ Author(s)_Name: Om Raheja & Mohit Rane
@ Date: 11 December 2019
@ Embedded Interface Design Super Project
@ The magic Wand
'''

# Imports
import pyaudio
import boto3
import wave


# Credentials required to create clients for services
access_key_id='ASIATHTWVR4QYPCGCGBQ'
secret_access_key='fcjBYIA0iKGnz65gW+tdFTFanDpQ7hpX0yZ6ILBR'
session_token='FwoGZXIvYXdzEL3//////////wEaDFEo24+7pqrl2Q/U3CLFAXVS4m8FOj8tFn9KfDlYJUgIHv8u+fnUdjESo1raJirWU4n3AtWhjuF1YGUuwSkB9gHWash0Vn62yaU2VmTUIIzl0AOBx5gjBElgL0ua7dTEQcwYS2sTO7BjujXYT9JehKqh3WhKlAaoED410cCHcIow6HnMnf9XItQrvJ+NAvDw2N3vt2A1nPKN8TYN27VNkRmv226C0rr+NiqqzNuVYt8zgUKcxsKybNFL699c2KA3LuvRqI+fyY3AHkYhgDih9eUkGPgNKJWHxe8FMi17wG7nvHcMg4epsKIQi2Mm3x2zLX7nYoxUYndNmzOj5JxShxQhFdcXlfa2/Bg='

# Global variables
form_1 = pyaudio.paInt16 	# 16-bit resolution
chans = 1 					# 1 channel
samp_rate = 48000 			# 48kHz sampling rate
chunk = 2 					# 2 samples for buffer
record_secs = 3 			# seconds to record
dev_index = 2 				# device index found by p.get_device_info_by_index(ii)
string = ''					# string variable to store data to be sent to SQS


# Client for Voice to text service [AWS Lex]
aws_lex_client=boto3.client('lex-runtime',\
						region_name='us-east-1',\
						aws_access_key_id=access_key_id,\
						aws_secret_access_key=secret_access_key,\
						aws_session_token=session_token)


'''
@ Function Name : record()
@ Brief         : Opens audio stream, read audio stream and save the audio file
@ Param in      : wav_output_filename
@ Return        : None 

'''

def record(wav_output_filename):
	print("Recording.....")
	frames = []
	
	# create pyaudio stream
	stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
						input_device_index = dev_index,input = True, \
						frames_per_buffer=chunk)
						
	# loop through stream and append audio chunks to frame array
	for ii in range(0,int((samp_rate/chunk)*record_secs)):
		data = stream.read(chunk,exception_on_overflow = False)
		if ii % 3 == 0:
			frames.append(data)
		
	print("Finished Recording!")
	
	# stop the stream, close it, and terminate the pyaudio instantiation
	stream.stop_stream()
	stream.close()
	
	# Save the audio file
	wavefile = wave.open(wav_output_filename,'wb')
	wavefile.setnchannels(chans)
	wavefile.setsampwidth(audio.get_sample_size(form_1))
	wavefile.setframerate(16000)
	wavefile.writeframes(b''.join(frames))
	wavefile.close()

	

'''
@ Function Name : speech_to_text_conversion()
@ Brief         : Input audio file, use AWS Lex to convert speech to text
@ Param in      : wav_output_filename
@ Return        : message_for_queue (Data to be sent to SQS) 

'''

def speech_to_text_conversion(wav_output_filename):
	print("Speech to text = " + wav_output_filename)
	wavefile = wave.open(wav_output_filename)

	text_response = aws_lex_client.post_content(botName='eid_test',\
														botAlias='stt',\
														userId='om',\
														contentType= "audio/l16; rate=16000; channels=1",\
														accept='text/plain; charset=utf-8',\
														inputStream=wavefile.readframes(96044))
					
	message_for_queue = text_response['ResponseMetadata']['HTTPHeaders']['x-amz-lex-message']
	print("Text = ",text_response['ResponseMetadata']['HTTPHeaders']['x-amz-lex-message'])
	print("Text = ",message_for_queue)
	return message_for_queue


audio = pyaudio.PyAudio() # create pyaudio instantiation
