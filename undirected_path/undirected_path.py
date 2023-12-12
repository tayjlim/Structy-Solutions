def undirected_path(edges, node_A, node_B):
  graph = makegraph(edges)
  return traverse(graph,node_A,node_B,set())
    
    
  """
  for this problem we make a directed graph
  and then we use the same logic to see if we have a path return True and False
  We want to 
  """
def traverse(graph,src,dst,visited):
  if src== dst:
    return True
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if traverse(graph,neighbor,dst,visited) == True:
      return True
  return False
​
def makegraph(edges):
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
    
      
      
  ('o', 'n')