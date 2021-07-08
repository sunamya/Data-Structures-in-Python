from collections import defaultdict
graph = defaultdict(list)
def addEdge(graph,u,v):
	graph[u].append(v)


def generate_edges(graph):
	edges = []
	for node in graph:
		for neighbour in graph[node]:
			edges.append([node, neighbour])
	return edges

addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','a')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

print("Graph : ",graph)

def find_all_paths(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return [path]
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
    for newpath in newpaths:
      paths.append(newpath)
  return paths

print(find_all_paths(graph, 'a', 'c'))
    