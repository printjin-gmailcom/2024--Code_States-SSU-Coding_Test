# https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3

from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for start, end in sorted(tickets):
        graph[start].append(end)

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=python3

from collections import deque

def solution(n, m, x, y, r, c, k):
    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    distance_to_target = abs(x - r) + abs(y - c)
    
    if distance_to_target > k or (k - distance_to_target) % 2 != 0:
        return "impossible"
    
    queue = deque([(x, y, "", k)])
    visited = set()
    
    while queue:
        x, y, path, remaining_moves = queue.popleft()
        
        if remaining_moves == 0:
            if (x, y) == (r, c):
                return path
        
        for direction, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= m and (nx, ny, remaining_moves - 1) not in visited:
                visited.add((nx, ny, remaining_moves - 1))
                queue.append((nx, ny, path + direction, remaining_moves - 1))
    
    return "impossible"

# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
    
    return network_count

# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):  
            if current_sum == target:
                return 1
            else:
                return 0
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    return dfs(0, 0)

# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3

def dfs(k, dungeons, visited):
    max_count = 0
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            max_count = max(max_count, 1 + dfs(k - dungeons[i][1], dungeons, visited))
            visited[i] = False
    return max_count

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, visited)