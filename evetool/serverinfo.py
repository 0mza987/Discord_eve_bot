import xml.etree.ElementTree as ET
from urllib.request import urlopen

def serverinfo():
	eveServer = 'https://api.eveonline.com//server/ServerStatus.xml.aspx'
	root = ET.fromstring(urlopen(eveServer).read())
	result = """Current server status:

EVE Time:	**{0}**
Server Open:	**{1}**
Players:		**{2}**
	""".format(root[0].text,root[1][0].text,root[1][1].text)
	return result