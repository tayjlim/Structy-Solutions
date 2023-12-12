from collections import deque
def shortest_path(edges, node_A, node_B):
  visited = set()
  graph = makeGraph(edges)
  print(graph)
  queue = deque([(node_A,0)])
  # node is node in graph:
  # print(graph[node_A]) # neighbors
  
  while queue:
    node, steps =  queue.popleft()
    visited.add(node)
    if node == node_B:
      return steps
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append((neighbor,steps+1))
  return -1
​
def makeGraph (edges): # this will maake the graph
  graph = {}
  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph
​
​
"""
  CYCLES 
  WE NEED A VISITED 
  BFS will return the shortest path from point a to point b because we explore its neighbors first
  This will use a qeueue a like data structure pushing the neighbors, and the CURRENT STEPS 
  1. make directed graph
  2. traverse
  popleft append 
"""