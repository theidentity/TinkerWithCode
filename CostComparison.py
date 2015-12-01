from bs4 import BeautifulSoup
import urllib2
import re

def get_page_contents():
	"""Returns contents of Kerala Gold Webpage"""
	url= 'http://www.keralagold.com/daily-gold-prices.htm'
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(),'html.parser')
	return soup

def get_yesterdays_cost(soup):
	"""Fetches the cost of Yesterday's prices and returns string"""
	all_spans_kg2=soup.findAll('span',{'class' : 'kg2'})
	cost_yesterday=all_spans_kg2[2].contents[0]
	return cost_yesterday

def get_todays_cost(soup):
	"""Fetches the cost of Today's prices and returns string"""
	all_spans_kg2b=soup.findAll('span',{'class' : 'kg2b'})
	cost_today=all_spans_kg2b[1].contents[0]
	return cost_today

def print_analysis(diff):
	if diff>0:
		print "Prices have increased by Rs.",diff
	elif diff<0:
		print "Prices have decreased by Rs.",(-diff)
	else:
		print "There is no change in prices"

def convert_to_integer(str1):
	""" String would be in the form Rs. 20,000.
	This function converts the comma seprated number to an integer"""
	str1=str1.replace(',', '')
	return int(re.findall("\d+", str1)[0])

soup=get_page_contents()
cost_yesterday=get_yesterdays_cost(soup)
cost_today=get_todays_cost(soup)
print "-----------------COST COMPARISON BY WEB CRAWLING-----------------"
print "Yesterday's cost \t: ",cost_yesterday
print "Today's cost \t\t: ",cost_today
diff=convert_to_integer(cost_today)-convert_to_integer(cost_yesterday)
print_analysis(diff)