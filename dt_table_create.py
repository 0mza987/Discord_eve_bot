import os
import sqlite3

def main():
	"""
	Create a system coordinate table:
		- coor_table.csv
	This table stores every system's coordinates to calculate the light year distance between two systems
	Need universeDataDx.db in ./resources/database

	:return: 
	"""
	db_dir = os.path.join("resources","database")
	db_file = os.path.join(db_dir,"universeDataDx.db")
	coor_table = os.path.join(db_dir,"coor_table.csv")
	cnt=0
	with sqlite3.connect(db_file) as sql_db:
		cursor = sql_db.cursor()
		result = cursor.execute('SELECT security, x, y, z, solarSystemName FROM mapSolarSystems')
		with open(coor_table,"w") as f_out:
			for row in result.fetchall():
				if row[0]> -0.99:
					cnt = cnt+1
					systemName = row[4]
					coor1 = row[1]/9460528450000000
					coor2 = row[2]/9460528450000000
					coor3 = row[3]/9460528450000000
					f_out.write("{},{},{},{},{}\n".format(systemName, row[0], coor1, coor2, coor3))
	print(cnt)




	# print(coord/9460528450000000)
	

if __name__ == "__main__":
	main()