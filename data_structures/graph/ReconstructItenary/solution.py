class GraphNode:
	def __init__(self, val):
		self.val = val
		self.adList = []
		self.visited = []

def insert(graph, src, dest):
	if src not in graph:
		graph[src] = GraphNode(src)
	if dest not in graph:
		graph[dest] = GraphNode(dest)
	index = 0
	for node in graph[src].adList:
		if node.val < dest:
			index += 1
		else:
			break
	graph[src].adList.insert(index, graph[dest])
	graph[src].visited.insert(index, False)

def getPath(graph, path):
	src = path[-1]
	node = graph[src]
	for i in range(len(node.adList)):
		if not node.visited[i]:
			node.visited[i] = True
			path.append(node.adList[i].val)
			return getPath(graph, path)
	return path

graph = {}
n = int(input())
for _ in range(n):
	src, dest = input().split()
	insert(graph, src, dest)
path = getPath(graph, [input()])
print(path if len(path) == n+1 else 'null')