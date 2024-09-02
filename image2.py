def solution(arr):
    arr = set(arr) 
    answer_case = set(range(1, 1 + len(arr)))
		
    if arr == answer_case:
        return True
    return False