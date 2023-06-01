def bfs(graph,start):

  queue=[start]
  node=queue.pop(0)
  neighbours = graph[node]
  return neighbours
graph = {'A': ['B', 'C']}  
print(bfs(graph,'A'))

