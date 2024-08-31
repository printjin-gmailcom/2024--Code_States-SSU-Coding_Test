# https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3

def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1
    
    max_score = max(scores)
    
    return [i + 1 for i, score in enumerate(scores) if score == max_score]

# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3

from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for perm in permutations(dungeons, len(dungeons)):
        current_fatigue = k
        count = 0
        for min_fatigue, fatigue_cost in perm:
            if current_fatigue >= min_fatigue:
                current_fatigue -= fatigue_cost
                count += 1
            else:
                break
        max_count = max(max_count, count)
    
    return max_count

# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
    return sum(absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes)))

# https://school.programmers.co.kr/learn/courses/30/lessons/152996?language=python3

from collections import Counter

def solution(weights):
    count = 0
    weight_count = Counter(weights)

    for weight in weight_count:
        if weight_count[weight] > 1:
            count += weight_count[weight] * (weight_count[weight] - 1) // 2
    
    for weight in weight_count:
        if weight * 2 / 3 in weight_count:
            count += weight_count[weight] * weight_count[weight * 2 / 3]
        if weight * 2 / 4 in weight_count:
            count += weight_count[weight] * weight_count[weight * 2 / 4]
        if weight * 3 / 4 in weight_count:
            count += weight_count[weight] * weight_count[weight * 3 / 4]

    return count