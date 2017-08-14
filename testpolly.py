import boto3
import subprocess
import os
import time

aws_access_key_id = os.environ['ACCESS_KEY'],
aws_secret_access_key = os.environ['SECRET_KEY'],
region_name='us-west-2'

d = time.strftime("%A %d")
m = time.strftime("%B")
t = time.strftime("%I:%M %p")
talk_to_me = "Hello Alberto! I would like to remind you that today is" + d +" of " + m + "and the time is " + t

polly = boto3.client('polly')

response = polly.synthesize_speech(
    OutputFormat='mp3',
    Text=talk_to_me,
    TextType='text',
    VoiceId='Joanna')

with open('hello.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())

subprocess.call(["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe","--play-and-exit","C:\\full\\path\\to\\hello.mp3"])

# Use the pygame module from within Linux or Raspberry Pi. Not MP3 support for MP3 on Windows
# pip install pygame
# from pygame import mixer # Load the required library
# mixer.init()
# mixer.music.load('hello.mp3')
# mixer.music.play()

# If you prefer CLI tools in Raspberry Pi are mpg123, mplayer and mpg321
# sudo apt-get install mpg123
# subprocess.call(["mpg123","filename.mp3"])
