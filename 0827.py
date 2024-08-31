# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3

from collections import deque, defaultdict

def solution(n, vertex):
    graph = defaultdict(list)
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque([1])
    visited = [-1] * (n + 1)
    visited[1] = 0  
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if visited[neighbor] == -1: 
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    
    max_distance = max(visited)
    return visited.count(max_distance)

# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    queue = deque([(0, 0)])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    return -1

# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3

from collections import deque

def solution(n, computers):
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in range(n):
                if computers[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_count += 1
    
    return network_count

# https://school.programmers.co.kr/learn/courses/30/lessons/159993?language=python3

from collections import deque

def bfs(start, target, maps):
    n, m = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == target:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    start = lever = exit = None
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
    
    to_lever = bfs(start, lever, maps)
    if to_lever == -1:
        return -1
    
    to_exit = bfs(lever, exit, maps)
    if to_exit == -1:
        return -1
    
    return to_lever + to_exit
