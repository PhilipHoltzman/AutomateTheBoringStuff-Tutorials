#! python 3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 10
while timeLeft > 0:
	print(timeLeft,end='')
	time.sleep(1)
	timeLeft = timeLeft - 1

# TODO at end of countdown play a sound file.

subprocess.Popen(['start', 'alarm.wav'], shell=True)