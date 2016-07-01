# coding: utf8
import requests
from bs4 import BeautifulSoup


o = open('test9.txt', 'w')
all_links = []
target = 'http://tvoyslot.com'

def homepage():
	r = requests.get(target)
	soup = BeautifulSoup(r.content, 'lxml')
	for link in soup.find_all('a'):
		if link.get('href')[0:4] != 'http' and len(link.get('href'))>1:
			print(link.get('href'))
			all_links.append(link.get('href'))
		elif link.get('href')[:len(target)] == target and len(link.get('href'))>1: 
			print(link.get('href'))
			all_links.append(link.get('href'))


def linker():
	for i in all_links:
		if i[0:4] == 'http' and i[0:4] != 'java':
			r = requests.get(i)
		elif i[0:4] != 'java':
			newi = target+i
			r = requests.get(newi)
		soup = BeautifulSoup(r.content, 'lxml')
		for link in soup.find_all('a'):
			try:
				if link.get('href')[0:4] != 'http' and len(link.get('href'))>1 and i[0:4] != 'java':
					if link.get('href') not in all_links:
						print(link.get('href'))
						all_links.append(link.get('href'))
				elif link.get('href')[:len(target)] == target and len(link.get('href'))>1 and i[0:4] != 'java':
					if link.get('href') not in all_links:
						print(link.get('href'))
						all_links.append(link.get('href'))
			except:
				pass


def pscraper():
	for link in set(all_links):
		#print(link)
		if link[0:4] == 'http' and link[0:4] != 'java':
			r = requests.get(link)
		else:
			newtarget = target + '/' + link
			r = requests.get(newtarget)
		soup = BeautifulSoup(r.content, 'lxml')
		for text in soup.find_all('p'):
			if len(text.text) >= 40:
				try:
					o.write(text.text+'\n')
				except:
					pass

#print(all_links)
#print(len(set(all_links)))
if len(all_links) == 0:
		homepage()
linker()
pscraper()
o.close()
