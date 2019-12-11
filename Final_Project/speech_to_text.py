import pyaudio
import boto3
import wave


access_key_id='ASIATHTWVR4QUUQ5T3ZX'
secret_access_key='kb/dMBxXuv6xghwr82LZng3liAVAzy1Y1kR+gnUp'
session_token='FwoGZXIvYXdzELr//////////wEaDJH7yKl1e4tEetY4byLFAWkFxnGxrsgwbgW71PtXAgKvVVBPSDJPf9DBnpy/saWlKP4pqn+X8irrafdRTgpCFEzm5AF/P1Xo8Ys8Gis8iBx9hXA+YB2zpUVlTgLRpjJ8khhpmAezM7e6auyWkzjNdxROE/Z6Lk2BC/hRvShYk/QPo6YGyBAJm0L3BYraRYYH2QIh3rHB3KMa2oOZznTeS+67vzOn+BRd2PCbYfjhRgDDa9Lz92x8QdAOWmtGfDmxhDb4OT7lTgOjKtwlWG9wbZnYx8LkKPWxxO8FMi1DSPJwLCuetzGjUpCSUaBz3mmAn/FxXF4O/xi2i5IHVXQyNlkOUgff85q3LRo='


form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 48000 # 48kHz sampling rate
chunk = 2 # 2 samples for buffer
record_secs = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
#wav_output_filename = 'command.wav' # name of .wav file
#frames = []
string = ''


aws_lex_client=boto3.client('lex-runtime',\
						region_name='us-east-1',\
						aws_access_key_id=access_key_id,\
						aws_secret_access_key=secret_access_key,\
						aws_session_token=session_token)

# Create SQS client
"""sqs = boto3.client('sqs',\
					region_name='us-east-1',\
					aws_access_key_id=access_key_id,\
					aws_secret_access_key=secret_access_key,\
					aws_session_token=session_token)
"""

#queue_url = 'https://sqs.us-east-1.amazonaws.com/222513434401/my_queue_project_3'


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
	wavefile = wave.open(wav_output_filename,'wb')
	wavefile.setnchannels(chans)
	wavefile.setsampwidth(audio.get_sample_size(form_1))
	wavefile.setframerate(16000)
	wavefile.writeframes(b''.join(frames))
	wavefile.close()


"""def save_audio(wav_output_filename):
	print("Filename = " + wav_output_filename)
	wavefile = wave.open(wav_output_filename,'wb')
	wavefile.setnchannels(chans)
	wavefile.setsampwidth(audio.get_sample_size(form_1))
	wavefile.setframerate(16000)
	wavefile.writeframes(b''.join(frames))
	wavefile.close()
"""
	
	
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
#	response = sqs.send_message(QueueUrl=queue_url,DelaySeconds=10,MessageBody=str(message_for_queue))
	return message_for_queue


audio = pyaudio.PyAudio() # create pyaudio instantiation
#record()
#save_audio()
#speech_to_text_conversion()
