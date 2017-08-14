# Python-AWS-Polly
Sample Python scripts to use AWS Polly service. This repo has been created as part of the Pied Piper program 2017
You can find a more elaborated discussion in here, including a short video of the code at work:

http://anzpiper.blogspot.com/2017/08/get-aws-polly-to-talk-to-you-from-python.html
## Usage
* Before starting make sure you install Boto3 module by running "*pip install boto3*"
* Then you need to ensure the AWS credentials are available to the script. You could accomplish this by means of:
  + Running the "*aws configure*" command if you have AWS CLI installed
  + Setting environment variables for access and secret keys
  + Creating an "*~/.aws/credentials*" file as follows. I couldn't find where the actual location for this file in Windows so I resorted to setting environment variables.
```SHELL
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
In this example I have used Windows and I am using VLC to play the file (you must use full paths to the VLC executable and to the MP3 file you want to play. Pygame is a more elegant solution with Python but apparently pygame doesn't have good support for MP3 on Windows 10 and I couldn't hear the file. However at the bottom you can sea comment section with the pygame sample code.

You can experiment with multiple voices. Please note that not all voices are available in all regions, so adjust the "region_name" variable accordingly
