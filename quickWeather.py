#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])


# TODO: Download the JSON data from the OpenWeatherMap.org API
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

response = requests.get(url)

response.raise_for_status()

# TAKING A BREAK UNTIL the 401 response is gone

# TODO: Load JSON data into a Python variable.