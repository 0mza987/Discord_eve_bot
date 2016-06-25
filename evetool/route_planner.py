import math
import sys
import pickle


def dijkstra(graph, source, dest, visited=set(),distance={}, predecessors={}):
	"""
	Calculate a shortest path from source to dest
	"""
	if source not in graph:
		raise TypeError('The source system cannot be found.')
	if dest not in graph:
		raise TypeError('The dest system cannot be found.')
	if source == dest:
		path=[]
		pred=dest
		while pred!=None:
			path.append(pred)
			pred=predecessors.get(pred,None)
		# print('route:', end=' ')
		# print(path)
		# print(distance[dest])
		# print(len(visited))
		# print(len(graph))
		return distance[dest]

	else:
		if not visited:
			distance[source]=0

		for neighbor in graph[source]:
			if neighbor not in visited:
				new_distance = distance.get(source,math.inf)+1
				if new_distance<distance.get(neighbor,math.inf):
					distance[neighbor]=new_distance
					predecessors[neighbor]=source
		# mark as visited
		visited.add(source)

		unvisited={}
		for k in graph:
			if k not in visited:
				unvisited[k]=distance.get(k,math.inf)
		x=min(unvisited,key=unvisited.get)
		return dijkstra(graph,x,dest,visited,distance,predecessors)

def route_plan(start, dest):
	"""
	"""
	sys.setrecursionlimit(10000)

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

	with open('resources/adjacent_graph.pickle','rb') as f:
		graph = pickle.load(f)
	res = dijkstra(graph, str(systemInfo[ssystem][0]), str(systemInfo[dsystem][0]), set(), {}, {})
	# return '{} {}'.format(systemInfo[ssystem][0],systemInfo[dsystem][0])
	reply='**{0} -> {1}** : {2} jumps'.format(ssystem, dsystem, res)
	return reply


# if __name__ == '__main__':
# 	sys.setrecursionlimit(10000)
# 	with open('resources/adjacent_graph.pickle','rb') as f:
# 		graph = pickle.load(f)
# 	res = -1
# 	res = dijkstra(graph,'30000001','30000023')
# 	print(res)











