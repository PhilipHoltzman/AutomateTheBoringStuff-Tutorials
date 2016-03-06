#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the programs instructions

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl-C to quit')

input()  # press enter to begin
print('Started..')
startTime = time.time() # get initial time for storage
lastTime = startTime
lapNum = 1


#TODO: Start tracking the lap times

try:
	while True:
		input()
		laptime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum,totalTime,laptime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time

except KeyboardInterupt:
	# Handle the Ctrl-C exveption to keep its error messsage from displaying.
	print('\nDone..')