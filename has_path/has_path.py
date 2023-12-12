def has_path(graph, src, dst):
  """
  return true or false
  recursively 
  """
  
  if src == dst:
    return True
  for neighbor in graph[src]:
    if has_path(graph,neighbor,dst) == True:
      return True
  return False 
    
    
  
 
  for neighbor in graph[node]: