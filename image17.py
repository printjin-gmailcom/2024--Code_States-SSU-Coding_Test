N = int(input())
H = list(map(int, input().split()))

width = [0] * N

for i in range(N):
    left = 0
    right = 0

    pos = i-1
    while pos >= 0 and H[pos] >= H[i]:
        left += 1
        pos -= 1
    
    pos = i+1
    while pos < N and H[pos] >= H[i]:
        right += 1
        pos += 1
    
    width[i] = left + right + 1

max_size = 0
answer = 0
for i in range(N):
		side = min(width[i], H[i])
		size = side**2
    if max_size < size:
        max_size = size
        answer = side
        
print(answer)