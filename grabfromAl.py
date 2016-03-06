#Grab Romeo from Al's website

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeroAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()
print('done')