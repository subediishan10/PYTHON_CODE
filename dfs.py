def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited

def dfs_start(graph,start):
    visited = []
    dfs(graph, start, visited)
    return visited

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print(dfs_start(graph, 'A'))


          
# Output: ['A', 'B', 'D', 'E', 'F', 'C']


