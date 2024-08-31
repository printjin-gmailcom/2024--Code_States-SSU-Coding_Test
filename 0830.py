# https://school.programmers.co.kr/learn/courses/30/lessons/92343?language=python3

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(node, sheep, wolf, visitable):
        nonlocal max_sheep
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if wolf >= sheep:
            return
        
        max_sheep = max(max_sheep, sheep)
        
        for next_node in visitable:
            next_visitable = visitable.copy()
            next_visitable.remove(next_node)
            next_visitable.extend(graph[next_node])
            dfs(next_node, sheep, wolf, next_visitable)
    
    max_sheep = 0
    dfs(0, 0, 0, graph[0])
    return max_sheep

# https://school.programmers.co.kr/learn/courses/30/lessons/87391?language=python3

def solution(n, m, x, y, queries):
    min_row, max_row = x, x
    min_col, max_col = y, y
    
    for command, dx in reversed(queries):
        if command == 0: 
            max_col = min(m - 1, max_col + dx)
            if min_col != 0:
                min_col += dx
        elif command == 1:  
            min_col = max(0, min_col - dx)
            if max_col != m - 1:
                max_col -= dx
        elif command == 2:  
            max_row = min(n - 1, max_row + dx)
            if min_row != 0:
                min_row += dx
        elif command == 3:  
            min_row = max(0, min_row - dx)
            if max_row != n - 1:
                max_row -= dx
        
        if min_row >= n or max_row < 0 or min_col >= m or max_col < 0:
            return 0
    
    return (max_row - min_row + 1) * (max_col - min_col + 1)

# https://school.programmers.co.kr/learn/courses/30/lessons/118668?language=python3

def solution(alp, cop, problems):
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(max_alp, i + alp_rwd)
                    new_cop = min(max_cop, j + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    
    return dp[max_alp][max_cop]

# https://school.programmers.co.kr/learn/courses/30/lessons/92342?language=python3

def solution(n, info):
    max_diff = -1
    best_shot = [-1]
    
    def calculate_score(ryan, apeach):
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if ryan[i] > apeach[i]:
                ryan_score += 10 - i
            elif apeach[i] > 0:
                apeach_score += 10 - i
        return ryan_score, apeach_score
    
    def backtrack(index, arrows_left, ryan_shot):
        nonlocal max_diff, best_shot
        
        if index == 11:
            if arrows_left > 0:
                ryan_shot[10] += arrows_left  
            ryan_score, apeach_score = calculate_score(ryan_shot, info)
            diff = ryan_score - apeach_score
            
            if diff > 0 and diff > max_diff:
                max_diff = diff
                best_shot = ryan_shot[:]
            elif diff > 0 and diff == max_diff:
                for i in range(10, -1, -1):
                    if ryan_shot[i] > best_shot[i]:
                        best_shot = ryan_shot[:]
                        break
                    elif ryan_shot[i] < best_shot[i]:
                        break
            if arrows_left > 0:
                ryan_shot[10] -= arrows_left  
            return
        
        if arrows_left > info[index]:
            ryan_shot[index] = info[index] + 1
            backtrack(index + 1, arrows_left - ryan_shot[index], ryan_shot)
            ryan_shot[index] = 0 
            
        backtrack(index + 1, arrows_left, ryan_shot)
    
    backtrack(0, n, [0] * 11)
    
    return best_shot

# https://school.programmers.co.kr/learn/courses/30/lessons/92341?language=python3

import math

def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def calculate_fee(time, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if time <= basic_time:
        return basic_fee
    else:
        extra_time = time - basic_time
        return basic_fee + math.ceil(extra_time / unit_time) * unit_fee

def solution(fees, records):
    in_times = {}
    total_times = {}
    
    for record in records:
        time, car_number, status = record.split()
        car_number = int(car_number)
        
        if status == "IN":
            in_times[car_number] = time_to_minutes(time)
        else: 
            in_time = in_times.pop(car_number)
            parked_time = time_to_minutes(time) - in_time
            if car_number in total_times:
                total_times[car_number] += parked_time
            else:
                total_times[car_number] = parked_time
    
    end_of_day = time_to_minutes("23:59")
    for car_number, in_time in in_times.items():
        parked_time = end_of_day - in_time
        if car_number in total_times:
            total_times[car_number] += parked_time
        else:
            total_times[car_number] = parked_time
    
    result = []
    for car_number in sorted(total_times.keys()):
        total_time = total_times[car_number]
        fee = calculate_fee(total_time, fees)
        result.append(fee)
    
    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/87390?language=python3

def solution(n, left, right):
    result = []
    for idx in range(left, right + 1):
        row = idx // n
        col = idx % n
        result.append(max(row, col) + 1)
    return result
