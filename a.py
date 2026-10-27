
import heapq



graph = {'S': {'A': 1, 'G': 10}, 'A': {'B': 2, 'C': 1}, 'B': {'D': 5},
'C': {'D': 3, 'G': 4}, 'D': {'G': 2}, 'G': {}}
heuristic = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0}

def a_star(graph,start,dest,h):
    pq=[(h[start],start,[start])]
    visited=set()
    while pq:
        f,node,path=heapq.heappop(pq)
        if node==dest:
            return path,f-h[dest]
        if node in visited:
            continue
        visited.add(node)
        for n,cost in graph[node].items():
            if n not in visited:
                g=(f-h[node])+cost
                heapq.heappush(pq,(g+h[n],n,path+[n]))
    return None,None




path, cost = a_star(graph, 'S', 'G', heuristic)
if path:
   print('Path:', ' -> '.join(path))
   print('Cost:', cost)
else:
   print('No path found')
