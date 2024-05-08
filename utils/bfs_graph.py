'''
图的遍历
'''

import collections

def bfs_graph_node(n, edges):
  G = collections.defaultdict(list)

  for u, v in edges:
    G[u].append(v)
    G[v].append(u)
  
  #define start node
  start = 0
  visited = {start: 0}   # here 0 represents distance from start

  queue = collections.deque([start])
  while queue:
    node = queue.popleft()
    
    #如果有明确的终点，可以在这里加终点的判断
    if node 是终点：
      break or return something
    
    for neighbor in G[node]:
      if neighbor in visited:
        continue
      queue.append(neighbor)
      visited[neighbor] = visited[node] + 1
  
  return something 

def bfs_graph_level(n, edges):
  G = collections.defaultdict(list)

  for u, v in edges:
    G[u].append(v)
    G[v].append(u)
  
  #define start node
  start_nodes = [0, 1, 2...]
  visited = {0: 0, 1: 0, 2: 0...}

  queue = [start_nodes]
  while queue:
    next_queue = []
    
    for node in queue:
      for neighbor in G[node]:
        if neighbor in visited:
          continue
        queue.append(neighbor)
        visited[neighbor] = visited[node] + 1
    
    queue = next_queue
  
  return something 