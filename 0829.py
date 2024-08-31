# https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        
        if number in dp[i]:
            return i
    
    return -1

# https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

# https://school.programmers.co.kr/learn/courses/30/lessons/161988?language=python3

def solution(sequence):
    n = len(sequence)
    
    pulse1 = [0] * n
    pulse2 = [0] * n
    
    for i in range(n):
        if i % 2 == 0:
            pulse1[i] = sequence[i]
            pulse2[i] = -sequence[i]
        else:
            pulse1[i] = -sequence[i]
            pulse2[i] = sequence[i]
    
    def max_subarray_sum(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    return max(max_subarray_sum(pulse1), max_subarray_sum(pulse2))

# https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3

def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    
    return max(land[-1])

# https://school.programmers.co.kr/learn/courses/30/lessons/12900?language=python3

def solution(n):
    MOD = 1000000007
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]

# https://school.programmers.co.kr/learn/courses/30/lessons/12907?language=python3

def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
            dp[i] %= 1000000007
    
    return dp[n]
