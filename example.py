import discord
import asyncio
import sqlite3
import csv
import os
import math
import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = 'https://api.eveonline.com//server/ServerStatus.xml.aspx'
url1='http://api.eve-central.com/api/marketstat?typeid=34&usesystem=30000142'

# headers = {'User-Agent':'Test use'}
# response = request.get(url,headers=hearders)
# root = ET.fromstring(urlopen(url1).read())
# data = tree.find('onlinePlayers')
# print(root)
# for point in root[0][0][1].findall('*'):
#     print(point, end=" ")
#     print(point.text)
# data = list(root.iter('onlinePlayers'))



def group(source):
    cnt = 0
    res = ''
    size = len(source)
    for x in range(size):
        res = res + source[size-x-1]
        cnt = cnt+1
        if cnt == 3 and not x==size-1:
            res=res+','
            cnt = 0
    return res[::-1]

a = 'wo cao ni mei'
print(a.split(2))




# coor_dir = os.path.join("resources","database")
# coor_table = os.path.join(coor_dir,"coor_table.csv")
# with open(coor_table,newline ='') as f_in:
#     csvreader = csv.reader(f_in,delimiter =",")
#     for row in csvreader:
#             if row[0].upper().startswith("raka".upper()):
#                 ssystem = row
#             elif row[0].upper().startswith("tama".upper()):
#                 dsystem = row

# x1, x2= float(ssystem[2]), float(dsystem[2])
# y1, y2= float(ssystem[3]), float(dsystem[3])
# z1, z2= float(ssystem[4]), float(dsystem[4])

# distance = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))

# a=1.2345678

# print(round(a,2))


# print(dsystem)
