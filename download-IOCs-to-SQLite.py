#!/usr/bin/python -u
#-*- coding:utf8 -*-
# Developed in Python 3.8.3, 2020-06-04 start of works.
# hacked 4 redamp company, 2020-06-04, see the readme in the repo for specs. 
#   /please refer xxFile(=readme.md) for xx~devProc=onboarding=hacking/tuning and usage. 

# To download files from net:
import requests 
# We will push data to SQLite via:
import sqlite3
# To store IPs as int(s) we use:
import ipaddress

#Try it out:
def PoC():
	listingsSources = "https://www.badips.com/get/list/any/2","http://reputation.alienvault.com/reputation.data","https://openphish.com/feed.txt"
	badIPs = listingsSources[1]#="https://www.badips.com/get/list/any/2"
	obtained=requests.get(badIPs)
	print( obtained.ok , obtained.reason, obtained.url )
	lines=obtained.text.splitlines() #todo rozvážit šetrnější iterátorz?.?(proč?)
	t=lines[:200]
	print(t)

#### Globals for quick tuning: ####
listingsSources = "https://www.badips.com/get/list/any/2","http://reputation.alienvault.com/reputation.data","https://openphish.com/feed.txt"
#categoriesOfSources = "IPs", "URLs"
sourcesAnotatedByCategory = {listingsSources[0]: "IPs", listingsSources[1]: "IPs", listingsSources[2]: "IPs"}
#todo: just tuple ,xx,yy = assignment
badIPs = listingsSources[0]#="https://www.badips.com/get/list/any/2"
badReputationIPsWithInfo = listingsSources[1]
phishyURLs = listingsSources[2]

# def parseDataset(dataset):
# 	# dataset is text=string
# 	lines=dataset.splitlines()
# 	return lines
#def extractIPfromBadReputationLine
def trimInfoFromBadReputationIPline(line):
	#return line[0:line.find('#')]#OK in our case, but struggles/bugs when no # sign found
	#  #something like [:(not -1 or None)] could be used, but thats piggy, better use split method:
	(firstField, *_) = line.split('#', maxsplit=1) #This is from my famous https://stackoverflow.com/a/40108965/266446 ;)
	return firstField

# For a quick tweaking/dev feedback we need:
def downloadDatasetToFile(sourceURL, fileHandle):
	obtained=requests.get(sourceURL)
	if obtained.ok :
		fileHandle.write(obtained.text)

# seems integrating httpie 'd be better but hack..:
def downloadDatasets():
	#helper function to avoid downloading on each use, to have offline testing and inspection capability
	#...[now draining from globals above]
	# if file exists..manually solved now
	with open("badIPs.txt", "w") as target:
		downloadDatasetToFile(badIPs, target)
	with open("badReputationIPsWithInfo.txt", "w") as target: #So this seems the most complicated, I could well just take the start and ignore all after # sign.
		downloadDatasetToFile(badReputationIPsWithInfo, target)
	with open("phishyURLs.txt", "w") as target:
		downloadDatasetToFile(phishyURLs, target)

def storeIPsStringsPoC():
	import sqlite3
	with open("badIPs.txt") as datasetTxt:
		#print( datasetTxt.read().splitlines()[:6]) #todo delete when cleaning or so
		introIPs = datasetTxt.read().splitlines()[:5]
	#now store that..:
	#sqlite3.connect()	
	import ipaddress #preferred to storing as TEXT or converting to Integers manually
	print(int(ipaddress.ip_address('1.2.3.4'))) 
	adrObj = ipaddress.ip_address(introIPs[0])
	internalAdrObj=int(adrObj)
	print(internalAdrObj) #looks good
	print(str(adrObj))

def IP2DbField(textIP):
	return int(ipaddress.ip_address(textIP))
def DbIP2text(dbFormatedIP):
	"""bevare, arg type must be ipaddress-*, not int class. Mostly expected to get arg of type 'ipaddress.IPv4Address'."""
	return str(dbFormatedIP)

def main():
	#PoC()
	#downloadDatasets()
	#storeIPsStringsPoC() #looks good, now @todo funcs IP2DbField and DbIP2text test also
	#print(trimInfoFromBadReputationIPline("NoSharpHere"), trimInfoFromBadReputationIPline("1.2.3.4"))# Works perfect with .split asigned to result, *_
	#print(trimInfoFromBadReputationIPline(open("badReputationIPsWithInfo.txt").readline()))

	## let's fake adding from each to see that works..:
	#print( *open("badIPs.txt").read().splitlines()[:6] ,sep='\n' ) #keepends=False is default on that one
	#print(trimInfoFromBadReputationIPline(open("badReputationIPsWithInfo.txt").readline()))
	#print( *open("phishyURLs.txt").read().splitlines()[:4] ,sep='\n' ) #keepends=False is default on that one 

	from dbImportPoC import tryOutCreatingDb;  tryOutCreatingDb() # Errs if db exists, which is not a problem now.
	from dbImportPoC import tryOutInsertingToDb;  tryOutInsertingToDb()

if __name__ == "__main__":
	main()
