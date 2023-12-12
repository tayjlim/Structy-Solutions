
from collections import deque
​
def knight_attack(n, kr, kc, pr, pc):
    visited = set([(kr, kc)])  # Make sure we don't backtrack
    queue = deque([(kr, kc, 0)])  # row, col, steps
​
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == (pr, pc):
            return steps
        
        for move in nextMoves(n, r, c):
            if move not in visited:
                visited.add(move)
                x, y = move
                queue.append((x, y, steps + 1))
​
    return None
​
  # deconstruct this because we are only x,y 
    
def nextMoves (n,r,c):
  moves= []
  positions = [
  (r+2,c+1), # xy (8 directions 2 up down left right, 1 up down left right)
  (r-2,c+1), 
  (r+2,c-1),
  (r-2,c-1),
  (r-1,c+2),
  (r+1,c-2),
  (r-1,c-2),
  (r+1,c+2)]
  
  for pos in positions:
    new_row, new_col = pos
    # IF IT IS IN BOUNDS 
    if 0<= new_row < n and 0<= new_col < n:
      moves.append(pos)
​
  
  return moves
​
​
#2 left 
# 2 right
#2up
#2 down
# n is tize of graph