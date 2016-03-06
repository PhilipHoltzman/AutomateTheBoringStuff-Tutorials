#! python3
# downloadXkcd.py - downloads every single XKCD comic

import requests, os, bs4 

url = 'http://xkcd.com'            # starting url

os.makedirs('C:\\pythonscripts\\xkcd', exist_ok=True) #store comcics in # dir
while not url.endswith('#'):

	# DL page

	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	# Find URL of the comic image
	comicElem = soup.select('#comic img')
	
	if comicElem == []:
		print('Could not find comic image..')
	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			#Download the image
			print('Downloading the image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()

		except requests.exceptions.MissingSchema:
			#skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue	


	# Download the image
	imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()


	# Get the Prev buttons URL
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')


print('Done..')