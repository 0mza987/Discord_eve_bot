import csv
import os
import math
import pickle

def inOneJump(start,dest):
	"""
	Determine if it's available for capital ships to jump between two systems.
	Need systemInfo.pickle in directory: resources/
	@parameters: start system, destination system
	:return: The results of the calculations
	"""
	with open('resources/systemInfo.pickle','rb') as f:
		systemInfo=pickle.load(f)

	ssystem=dsystem=0
	# find coordinates for the two input systems
	systemNames=list(systemInfo.keys())
	for system in systemNames:
		if system.lower().startswith(start.lower()):
			ssystem=system
		elif system.lower().startswith(dest.lower()):
			dsystem=system
	if not ssystem or not dsystem:
		return '__At least one of the system names is NOT correct!__'
	x1, y1, z1= systemInfo[ssystem][1], systemInfo[ssystem][2], systemInfo[ssystem][3]
	x2, y2, z2= systemInfo[dsystem][1], systemInfo[dsystem][2], systemInfo[dsystem][3]
	# calculate the distance between two systems in light years
	distance = round(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2)),2)

	res=[]
	# res[0] for Carriers, Dreadnoughts, FAX
	# res[1] for Titans, Supercarriers 
	# res[2] for Jumpfreighters, Rorquals
	# res[3] for Black ops
	benchmarks = [[6.5,7],[5.5,6],[9,10],[7.2,8]]
	for i in range(4):
		if distance <= benchmarks[i][0]:
			ss='JDC4, JDC5'
		elif distance <=benchmarks[i][1]:
			ss='JDC5'
		else:
			ss='Negative'
		res.append(ss)
	result = """__**{0} -> {1}({2}ly)**__:

__Carriers__: {3}
__Dreadnoughts__: {3}

__Titans__: {4}
__Supercarriers__: {4}

__Jumpfreighters__: {5}
__Rorquals__: {5}

__Black Ops__: {6}
	""".format(ssystem,dsystem,distance,res[0],res[1],res[2],res[3])
	return result
