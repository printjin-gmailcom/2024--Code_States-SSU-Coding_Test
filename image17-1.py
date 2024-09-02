N = int(input())
H = list(map(int, input().split()))

left = [0] * N
right = [0] * N
stack = []

for i, h in enumerate(H):
    while stack and stack[-1][1] > h:
        pi, ph = stack.pop()
        right[pi] = i - pi -1
    stack.append((i, h))

while stack:
    pi, ph = stack.pop()
    right[pi] = N - pi -1

for i, h in enumerate(reversed(H)):
    while stack and stack[-1][1] > h:
        pi, ph = stack.pop()
        left[N-1-pi] = i - pi -1
    stack.append((i, h))

while stack:
    pi, ph = stack.pop()
    left[N-1-pi] = N - pi -1


width = [0]*N
for i in range(N):
    width[i] = left[i] + 1 + right[i]


max_size = 0
answer = 0
for i in range(N):
    if max_size < width[i]*H[i]:
        max_size = width[i]*H[i]
        answer = H[i]
        
print(answer)
