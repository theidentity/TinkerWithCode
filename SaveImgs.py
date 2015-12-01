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

def get_images(soup):
	ImageContainers = soup.findAll("p", {"class":"imgC"})
	for imgcnt in ImageContainers:
		imgUrl = imgcnt.img['src']
		imgName = (imgUrl.rsplit('/'))[6]
		print imgName,
		f = open("Images/"+imgName,'wb')
		f.write(urllib.urlopen(imgUrl).read())
		f.close()
		print "Completed"

soup = get_page_contents()
get_images(soup)

