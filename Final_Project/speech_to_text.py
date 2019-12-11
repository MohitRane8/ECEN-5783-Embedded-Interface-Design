import pyaudio
import boto3
import wave


access_key_id='ASIATHTWVR4QZ5PC7Y5C'
secret_access_key='2Dn4ajXWKfyogg7RigqD0lXYYvR8Zxuv+v509jqY'
session_token='FwoGZXIvYXdzEKr//////////wEaDLq4ExNRDRYmKevldyLFAcF9QiQh/QqTXdWIQewrSy7smyQ47ZwDWnJ6Mis30+saLGmI8T+Nhk9s/4fAUTybywTZmZ0TLvREvH9NdgmjDbQhY8zk5zoIAdQYqPM9luDeFvilgbKtag6YShCB+nCymHOnuRbvv8HO0icSiqTPgs2819LUKznCjjveKF5cQRCLsmI04hlO3g6/LcrvpHf+qcYL/xvz2fh37byXzeMcCCSTzottOZ78DpheP+F3s2X0q1sP+8lb4OiG4WtsQt7JBYWPo9e4KMzrwO8FMi1j3/W3asfBuZYbv8MP2rKuEQLrMfamtHhEd4bvdj7G7R/FJzbej5RbQuYoNZ8='



form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 48000 # 48kHz sampling rate
chunk = 512 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'command.wav' # name of .wav file
frames = []


def record():
	print("Recording.....")
	
	# create pyaudio stream
	stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
						input_device_index = dev_index,input = True, \
						frames_per_buffer=chunk)
						
	# loop through stream and append audio chunks to frame array
	for ii in range(0,int((samp_rate/chunk)*record_secs)):
		data = stream.read(chunk)
		if ii % 6 == 0:
			frames.append(data)
		
	print("Finished Recording!")
	
	# stop the stream, close it, and terminate the pyaudio instantiation
	stream.stop_stream()
	stream.close()
	audio.terminate()


def save_audio():
	wavefile = wave.open(wav_output_filename,'wb')
	wavefile.setnchannels(chans)
	wavefile.setsampwidth(audio.get_sample_size(form_1))
	wavefile.setframerate(samp_rate)
	wavefile.writeframes(b''.join(frames))
	wavefile.close()
	
	
	
def speech_to_text_conversion():
	aws_lex_client=boto3.client('lex-runtime',\
						region_name='us-east-1',\
						aws_access_key_id=access_key_id,\
						aws_secret_access_key=secret_access_key,\
						aws_session_token=session_token)

	wavefile = wave.open(wav_output_filename)
						#lexruntimeservice_
	text_response = aws_lex_client.post_content(botName='eid_test',\
														botAlias='stt',\
														userId='om',\
														contentType= "audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false",\
														accept='text/plain; charset=utf-8',\
														inputStream=wavefile.readframes(48172))
														
	print("Text = ",text_response['ResponseMetadata']['HTTPHeaders']['x-amz-lex-message'])


audio = pyaudio.PyAudio() # create pyaudio instantiation
record()
save_audio()
speech_to_text_conversion()
