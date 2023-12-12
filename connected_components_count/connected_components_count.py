
def connected_components_count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    # print (node)# this is current 
    # print(graph[node])  this is the neighbors 
    if traverse(graph,node,visited) == True:
      count +=1 #increment the answer 
  return count # return the count
​
def traverse(graph, current,visited):
  # this function is recursively going to go through the neighbors. makring them as visited and 
  
  if current in visited:
    return False
  visited.add(current)
  for neighbor in graph[current]:
    traverse(graph,neighbor,visited) # once we go through all the neighbors without reaching a NEW VISITED NODE
    # this means we have completed one island
    
  return True # this function will return true IF THIS IS A NEW ISLAND NOT EXPLORED
  
​
  ('o', 'n')