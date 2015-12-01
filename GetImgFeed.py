from bs4 import BeautifulSoup
import os
import urllib
import urllib2
import re

def get_page_contents():
	"""Returns contents of the Webpage"""
	url= 'http://abduzeedo.com/logo-design-work-rob-clarke'
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(),'html.parser')
	return soup

def get_Imgs(soup):
	"""Extracts URLs of all images in newsfeed"""
	print
	print '\t\t***Extraction Begins***'
	ImageContainers = soup.findAll("p", {"class":"imgC"})
	for imgcnt in ImageContainers:
		imgUrl = imgcnt.img['src']
		download(imgUrl)
	print
	print '\t\t***Extraction Completed***'

def download(imgUrl):
	"""Downloads the images indicated in imgUrl"""
	file_name = imgUrl.split('/')[-1]
	u = urllib2.urlopen(imgUrl)
	f = open("Images/"+file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size),
	print "Completed"

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,
	f.close()

soup = get_page_contents()
get_Imgs(soup)




