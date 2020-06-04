#!/usr/bin/python -u
#-*- coding:utf8 -*-
# Developed in Python 3.8.3, 2020-06-04 start of works.
# hacked 4 redamp company, 2020-06-04, see the readme in the repo for specs. 
#   /please refer xxFile for xx~devProc and usage. 

#to download files from net:
import requests 
#we will push data to sqLite via:
import sqlalchemy


#Try it out:
def PoC():
	ipLines = "https://www.badips.com/get/list/any/2"
	obtained=requests.get(ipLines)
	print( obtained.ok , obtained.reason, obtained.url )
	print("sqlalchV:",sqlalchemy.__version__ )
	
def main():
	PoC()
	
if __name__ == "__main__":
	main()
