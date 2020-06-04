#!/usr/bin/python -u
#-*- coding:utf8 -*-
# Developed in Python 3.8.3, 2020-06-04 start of works.
# hacked 4 redamp company, 2020-06-04, see the readme in the repo for specs. 
#   /please refer xxFile(=readme.md) for xx~devProc=onboarding=hacking/tuning and usage. 

#to download files from net:
import requests 
#we will push data to SQLite via:
#import sqlite3

#Try it out:
def PoC():
	listingsSources = "https://www.badips.com/get/list/any/2","http://reputation.alienvault.com/reputation.data","https://openphish.com/feed.txt"
	badIPs = listingsSources[1]#="https://www.badips.com/get/list/any/2"
	obtained=requests.get(badIPs)
	print( obtained.ok , obtained.reason, obtained.url )
	lines=obtained.text.splitlines() #todo rozvážit šetrnější iterátorz?.?(proč?)
	t=lines[:200]
	print(t)

def parseDataset(dataset):
	# dataset is text=string
	lines=dataset.splitlines()
	return lines

# For a quick tweaking/dev feedback we need:
def downloadDatasetToFile(sourceURL, fileHandle):
	obtained=requests.get(sourceURL)
	if obtained.ok :
		fileHandle.write(obtained.text)

# seems integrating httpie 'd be better but hack..:
def downloadBadIPs():
	#helper function to avoid downloads, have offline testing capability
	listingsSources = "https://www.badips.com/get/list/any/2","http://reputation.alienvault.com/reputation.data","https://openphish.com/feed.txt"
	badIPs = listingsSources[0]#="https://www.badips.com/get/list/any/2"
	# if exists..manually solved now
	with open("badIPs.txt", "w") as target:
		downloadDatasetToFile(badIPs, target)

def main():
	#PoC()
	downloadBadIPs()

if __name__ == "__main__":
	main()
