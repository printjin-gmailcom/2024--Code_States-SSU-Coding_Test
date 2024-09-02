from collections import deque

def solution(N, mine, P):
    game_map = [[0]*(N+1) for _ in range(N+1)]
    visited = [[False]*(N+1) for _ in range(N+1)]
	
    for x, y in mine:
        game_map[x][y] = 1

    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1),
                    (1, 0), (1, 1), (0, 1), (-1, 1)]
    for x, y in mine:
        for dx, dy in directions:
            if not(1 <= x+dx <= N) or not(1 <= y+dy <= N):
                continue
            if game_map[x+dx][y+dy] != 1:
                game_map[x+dx][y+dy] = 2
    
    queue = deque([])
    queue.append(P)

    cnt = -1
    while queue:
        x, y = queue.popleft()
        cnt += 1
				
        if game_map[x][y] == 2:
            continue

        for dx, dy in directions:
            if not(1 <= x+dx <= N) or not(1 <= y+dy <= N):
                continue
            if not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                queue.append((x+dx, y+dy))
    
    return cnt