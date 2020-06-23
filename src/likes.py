#!usr/bin/python2.7
# coding=utf-8

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	post = raw_input('\n\033[1;96mEnter post url:\033[1;90m ')
	try:
		domain = post.split('//')[1].split('/')[0]
		post = post.replace(domain, 'mbasic.facebook.com')
	except IndexError:
		exit('\n\033[0;91mInvalids url!\033[0m')
	url_likes = None
	response = config.httpRequest(post, cookie).encode('utf-8')
	html = parser(response, 'html.parser')
	for x in html.find_all('a'):
		if '/ufi/reaction/profile/browser/?' in x['href']:
			url_likes = url+x['href']
			break
	if url_likes == None:
		exit('\n\033[0;91mNot found :(\033[0m')
	try:
		max = int(raw_input('\033[1;92mHow many? \033[1;93m(ex: 5000): '))
	except ValueError:
		exit("\n\033[0;91mStuppid.\033[0m")
	if max == 0:
		exit("\n\033[0;91mRequired, can't empty.\033[0m")

	statusStop = False
	output = 'dump/likes.json'
	id = []
	print('')

	while True:
		try:
			response = config.httpRequest(url_likes, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			find = html.find_all('h3')
			for i in find:
				full_name = i.text.encode('utf-8')
				href = i.find('a')
				if '+' in str(href) or href == None:
					continue
				else:
					if 'profile.php?id=' in str(i):
						uid = re.findall('\/profile.php\?id=(.*?)$', href['href'])
					else:
						uid = re.findall('\/(.*?)$', href['href'])
					if len(uid) == 1:
						id.append({'uid': uid[0].replace('/',''), 'name': full_name})
					sys.stdout.write("\r - %s                                        \r\n\033[1;94m[\033[0;96m%s\033[1;94m] [\033[0;96m%s\033[1;94m] \033[1;91mDon't close."%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
					if len(id) == max or len(id) > max:
						statusStop = True
						break
			if statusStop == False:
				if 'View more' in str(html):
					url_likes = url+html.find('a', string='View more')['href']
				else: break
			else: break
		except KeyboardInterrupt:
			print('\n\n\033[0;91mKeyInterrupt, stopped!!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\nOutput: '+output)
	save = open(output, 'w')
	save.write(json.dumps(id))
	save.close()
