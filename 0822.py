# https://school.programmers.co.kr/learn/courses/30/lessons/12978?language=python3

import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    queue = [(0, 1)]
    
    while queue:
        current_time, current_village = heapq.heappop(queue)
        
        if current_time > dist[current_village]:
            continue
        
        for neighbor, travel_time in graph[current_village]:
            new_time = current_time + travel_time
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(queue, (new_time, neighbor))
    
    return sum(1 for time in dist if time <= K)

 #https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        mix_count += 1
    
    return mix_count

# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3

import heapq
from collections import defaultdict, deque

def solution(n, vertex):
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1:  
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
    
    max_distance = max(distances)
    return distances.count(max_distance)

# https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3

def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    
    answer = 0
    for i in range(1, n + 1):
        if graph[i].count(0) == 2: 
            answer += 1
    
    return answer
