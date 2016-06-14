import csv
import os
import xml.etree.ElementTree as ET
from urllib.request import urlopen

eveServer = 'https://api.eveonline.com//server/ServerStatus.xml.aspx'
eve_central = 'http://api.eve-central.com/api/marketstat?typeid=34&usesystem=30000142'

def howmuch(item,system):
	"""
	Check item price of a specific system

	@param: item name, solar system name
	:return: the result of the price check
	"""
	typeid_table = os.path.join('resources','typeids.csv')
	itemID = -1
	with open(typeid_table,newline='') as f_in:
		csvreader = csv.reader(f_in,delimiter = ',')
		for row in csvreader:
			if row[1].lower()==item.lower():
				item = row[1]
				itemID = row[0]
				break
	if item.lower()=='plex':
		itemID=29668
		item='PLEX'
	if itemID == -1:
		return '__Item not found.__'

	systems = {'Jita': 30000142, 'OSY-UD':30001005}
	systemID = systems[system]
	apiaddress = 'http://api.eve-central.com/api/marketstat?typeid={0}&usesystem={1}'.format(itemID,systemID)
	root = ET.fromstring(urlopen(apiaddress).read())
	result = """Item: **{0}**. System: **{1}**

__Sell__: {2}  isk
__Buy__: {3}  isk
	""".format(item,system,group(root[0][0][1][3].text),group(root[0][0][0][2].text))
	return result

def group(source):
	"""
	To group the numbers up, make xxxxxxxx.00 become xx,xxx,xxx.00
	"""
	cnt = 0
	res = ''
	size = len(source)
	for x in range(3,size):
		res = res + source[size-x-1]
		cnt = cnt+1
		if cnt == 3 and not x==size-1:
			res=res+','
			cnt = 0
	res=res[::-1]+source[size-3:size]
	return res
