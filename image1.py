from itertools import combinations

def chk_prime(n):
	for i in range(2, n):
		if n % i ==  0: 
			return False

	return True 
	
def solutions(nums):
	answer = 0
	
	for comb in combinations(nums, 3):
		value = sum(comb)
		if chk_prime(value):
			answer += 1

	return answer