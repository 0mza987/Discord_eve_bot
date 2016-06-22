import math
import sys
import pickle

if __name__=='__main__':
	"""
	Create a pickle file to store dijkstra results in /resources/:
		- dijkstra_results.pickle
	Results are stored in a dict,(e.g.):
		{'30000001': {'30000002':2, '30000003':4, ...}, ...}
	Need adjacent_graph.pickle in directory /resources
	Warning: the size of result file will be more than 200 MB, that also means running this script will take a pretty long time
	"""
	sys.setrecursionlimit(10000)
	dijkstra_results ={}
	with open('resources/adjacent_graph.pickle','rb') as f:
		graph = pickle.load(f)

	systemList=list(graph.keys())
	for system in systemList:
		dijkstra(graph,system,system,0, dijkstra_results)
	with open('dijkstra_results.pickle','wb') as f:
		pickle.dump(dijkstra_results,f)


def dijkstra(graph, source, key, cnt, res, visited=set(),distance={}, predecessors={}):
	"""
	Calculate a shortest path from source to dest
	"""
	if source not in graph:
		raise TypeError('The source system cannot be found.')
	# if dest not in graph:
	# 	raise TypeError('The dest system cannot be found.')
	# if source ==dest:
	# 	path=[]
	# 	pred=dest
	# 	while pred!=None:
	# 		path.append(pred)
	# 		pred=predecessors.get(pred,None)
	# 	print('route:', end=' ')
	# 	print(path)
	# 	print(distance[dest])
	# 	print(cnt)
	# 	print(len(visited))
	# 	print(len(graph))
	if len(visited)==len(graph):
		jumps ={}
		for system in visited:
			if system!=key:
				jumps[system]=distance.get(system,math.inf)
		res[key]=jumps
				
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
		if unvisited:
			x=min(unvisited,key=unvisited.get)
			cnt=cnt+1
			dijkstra(graph,x,key,cnt,res,visited,distance,predecessors)
		else:
			dijkstra(graph,source,key,cnt,res,visited,distance,predecessors)
