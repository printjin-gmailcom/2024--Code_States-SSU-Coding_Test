def solution(record):
	answer = 0
	remains = 0
	
	for rec in record:
		remains += rec
		if remains < 0:
			answer += 1
	
	return answer