from collections import deque

def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1
    
    graph = [[] for _ in range(n)]
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * n
    num_components = 0
    
    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            while queue:
                x = queue.popleft()
                visited[x] = True
                for neighbor in graph[x]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
            num_components += 1
    
    return num_components - 1


print(makeConnected(6,[[0,1],[0,2],[0,3],[1,2],[1,3]]))
