import subprocess

import time
import subprocess
import RPi.GPIO as GPIO
input_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)

while True:
	if (GPIO.input(input_pin)):
		print('Button Pressed')
		print("Get ready with your webcam")
		print('Taking snap in next 10seconds')
		time.sleep(10)	
		print("Taking snap")
		subprocess.call(['fswebcam', '-r', '720x340', 'example.jpg'])
		print("Thresholding image")
		subprocess.call(['convert', './example.jpg', '-threshold', '+20%', 'speech.jpg'])
		print("Performing OCR")
		subprocess.call(['tesseract', 'speech.jpg', 'speech'])
		print("The detected text is")
		subprocess.call(['cat', 'speech.txt'])
		print("Speaking text")
		subprocess.call(['festival', '--tts', 'speech.txt'])
GPIO.cleanup()

