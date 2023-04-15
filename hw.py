from collections import deque

def visit(rooms):
    n = len(rooms)
    visited = [False] * n  
    visited[0] = True  
    queue = deque([0]) 

    while queue:
        room = queue.popleft()
        for key in rooms[room]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

print(visit([[1,3],[3,0,1],[2],[0]]))