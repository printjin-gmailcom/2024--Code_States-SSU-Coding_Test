def solution(src):
	answer = ""
	answer += src[0]
	
	counts = []
	
	pre = src[0]
	cnt = 1
	for char in src[1:]:
		if char != pre:
			counts.append(cnt)
			cnt = 1
		else:
			cnt += 1
		pre = char

	counts.append(cnt)
	alphbet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
						 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
						 "W", "X", "Y", "Z"]
	
	for cnt in counts:
		answer += alphabet[cnt-1]
	return answer