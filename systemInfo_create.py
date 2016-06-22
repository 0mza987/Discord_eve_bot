import os
import sqlite3
import pickle

def main(systemInfo):
	"""
	Create a system information dict:
		{solarSystemName : [solarSystemID, x, y, z, security]}
		(e.g.):
		{'Jita':[30000142, -13.642457968072414, 6.42197814118551, 12.416772242790548, 0.9459131166648389]}
	:return: 
	"""
	db_dir = os.path.join("resources","database")
	db_file = os.path.join(db_dir,"universeDataDx.db")
	cnt=0
	with sqlite3.connect(db_file) as sql_db:
		cursor = sql_db.cursor()
		result = cursor.execute('SELECT security, x, y, z, solarSystemName, solarSystemID FROM mapSolarSystems')
		for row in result.fetchall():
			if row[0]> -0.99:
				info=[]
				cnt = cnt+1
				coor1 = row[1]/9460528450000000
				coor2 = row[2]/9460528450000000
				coor3 = row[3]/9460528450000000
				info.append(row[5])
				info.append(coor1)
				info.append(coor2)
				info.append(coor3)
				info.append(row[0])
				systemInfo[row[4]]=info
	print(cnt)


	# print(coord/9460528450000000)
	

if __name__ == "__main__":
	systemInfo = {}
	main(systemInfo)
	with open('resources/systemInfo.pickle','wb') as f:
		pickle.dump(systemInfo,f)