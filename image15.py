def solution(arr, k):
	cols = len(arr[0])
	rows = len(arr)
	
	if k == 0:
		return arr
	if cols == 1 and rows == 1:
		return arr
	
	if cols >= rows:
		answer = [[] for _ in range(rows)]
		
		for i in range(rows):
			for j in range(cols//2):
				answer[i].append(max(arr[i][2*j], arr[i][2*j+1]))
	
	else:
		answer = [[] for _ in range(rows//2)]
		
		for i in range(cols):
			for j in range(rows//2):
				answer[j].append(min(arr[2*j][i], arr[2*j+1][i]))
				
	return solution(answer, k-1)