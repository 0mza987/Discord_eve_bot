import csv
import os
import pickle

def main():
	"""
	Create a adjacent graph and store it as a pickle file:
		adjacent_graph.pickle
	Need system_jumps.csv in ./resources
	"""
	adjacent_graph={}
	neighbors = []
	last_system =''
	connections = os.path.join('resources','system_jumps.csv')

	with open(connections,newline='') as f_in:
		csvreader=csv.reader(f_in,delimiter=';')
		for row in csvreader:
			if last_system!='' and row[0]!=last_system:
				adjacent_graph[last_system]=neighbors
				neighbors=[]
			neighbors.append(row[1])
			last_system=row[0]
		adjacent_graph[last_system]=neighbors
	with open('resources/adjacent_graph.pickle','wb') as f:
		pickle.dump(adjacent_graph,f)
		
if __name__ == '__main__':
	main()
