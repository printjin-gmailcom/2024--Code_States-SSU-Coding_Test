# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    result = []
    for num in arr:
        if not result or result[-1] != num:
            result.append(num)
    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    result = []
    
    current_deploy_day = days[0]
    count = 0
    
    for day in days:
        if day <= current_deploy_day:
            count += 1
        else:
            result.append(count)
            count = 1
            current_deploy_day = day
    
    result.append(count)
    
    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3

from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            order += 1
            if current[1] == location:
                return order

# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices):
    n = len(prices)
    result = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            result[i] += 1
            if prices[i] > prices[j]:
                break
    
    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3

from collections import deque

def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    
    if total_sum % 2 != 0:
        return -1
    
    target_sum = total_sum // 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    n = len(queue1)
    max_operations = n * 3
    operations = 0
    
    i, j = 0, 0
    
    while i < max_operations and j < max_operations:
        if sum1 == target_sum:
            return operations
        elif sum1 > target_sum:
            val = q1.popleft()
            q2.append(val)
            sum1 -= val
            sum2 += val
            i += 1
        else:
            val = q2.popleft()
            q1.append(val)
            sum1 += val
            sum2 -= val
            j += 1
        
        operations += 1
    
    return -1